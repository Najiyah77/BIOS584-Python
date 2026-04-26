#-------------------------------------------------------------
# Name:
# This script performs 4 types of analyses: multiple linear regression,
# multiple logistic regression with forest plots, chi-square and t-test
#---------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os
from statsmodels.formula.api import ols
import statsmodels.api as sm
from scipy import stats
from statsmodels.formula.api import logit
from scipy.stats import chi2_contingency

#Set working directory
print(os.getcwd()) #get current working directory
os.chdir(r'C:\Users\Najiy\OneDrive\Desktop\PycharmProjects\BIOS584-Python\Skin Cancer') #set working directory (change it to your filename)
#Read in cleaned data created from 0_SkinCancer_Cleaning
skc = pd.read_excel("cleaned_skc.xlsx")
skc_cc = pd.read_excel("cleaned_skc_cc.xlsx")
skc.info()
skc_cc.info()
skc.columns

#---------------------------------------------------------------------------------
# Simple Linear Regression
#---------------------------------------------------------------------------------
#Reference level by default is chosen based on alphabetical order of the category names.
# So here POC is the reference, and White is the "treatment level"
ttd_race_lr = ols("m1_time_to_diagnosis ~ Race_binary", data = skc_cc).fit()
ttd_race_lr.summary()

#Hardcode the reference level to be white and redo regression
ttd_race_lr2 = ols("m1_time_to_diagnosis ~ C(Race_binary, Treatment(reference='White'))",
                  data=skc_cc).fit() #reference is white, POC is treatment
ttd_race_lr2.summary()

#---------------------------------------------------------------------------
# T-test with side by side boxplots
#---------------------------------------------------------------------------
#Simple linear regression with a binary predictor is equivalent to a t-test
skc_cc.groupby('Race_binary')['m1_time_to_diagnosis'].mean() #quick group means

 #Welch independent t-test (assumes unequal variance)
#Side by side boxplot
skc_cc.boxplot(column='m1_time_to_diagnosis', by='Race_binary')
plt.title("Time to Diagnosis by Race")
plt.suptitle("") #gets rid of ugly default pandas title
plt.xlabel("Race")
plt.ylabel("Time To Diagnosis")
plt.show()

#Seaborn version of boxplot - it is prettier!
sns.boxplot(x='Race_binary', y='m1_time_to_diagnosis', data=skc_cc)
plt.title("Time to Diagnosis by Race")
plt.show()

#-------------------------------------------------------------------------------
#  Multiple linear regression
#-------------------------------------------------------------------------------
ttd_mlr = ols("m1_time_to_diagnosis ~ C(Race_binary, Treatment(reference='White')) +"
              "prior_skin_cancer + M1_Location_risk + cancer_type + Gender + "
              "num_primary_malignancies", data=skc_cc).fit() #fill this in with me
ttd_mlr.summary()
#To add an interaction, do "+ prior_skin_cancer: num_primary_malignancies"

#----- Check diagnostics of the linear model -----
#Residual plot
plt.figure()
plt.scatter(ttd_mlr.fittedvalues, ttd_mlr.resid)
plt.axhline(0, linestyle="--")
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()

#QQ-plot
sm.qqplot(ttd_mlr.resid, line='45')
plt.show() # lol this model does not fit the data

#Cook's distance
influence = ttd_mlr.get_influence()
cooks_d = influence.cooks_distance[0] #this returns 2 arrays: cook's d array and p-values array
#Let's extract just the first cook's distance array so use [0]
n = len(skc_cc)
threshold = 4 / n #typical threshold to identify influential points
plt.figure()
plt.scatter(range(n), cooks_d)
plt.axhline(threshold, linestyle="--")
plt.xlabel("Observation Index")
plt.ylabel("Cook's Distance")
plt.title("Cook's Distance")
plt.show()

#See some influential points - investigate
influential = cooks_d > (4 / len(cooks_d))
#data of people with influential points
skc_cc[influential]

 #data of people WITHOUT influential points
skc_cc[~influential] # getting rid of the influential

#Can re-run regression without influential points to investigate
#how the regression line and results change. Don't blindly remove points though

#-------------------------------------------------------------------------------
# Chi-square
#-------------------------------------------------------------------------------
skc["M1_Location_risk"].value_counts()
#See frequency table
table = pd.crosstab(skc['Race_binary'], skc['M1_Location_risk'], normalize = True) # the normalize gives you a percentage
print(table)

 #check expected counts for assumptions, 80% of cells should be >5
chi2, p, dof, expected = chi2_contingency(table)

#Barchart
table.plot(kind='bar')
plt.xlabel("Race")
plt.ylabel("Count")
plt.title("Side-by-Side Bar Chart")
plt.xticks(rotation=0) #makes the x labels horizontal
plt.show()

#-------------------------------------------------------------------------------
# Logistic Regression with Forest Plot
#-------------------------------------------------------------------------------
#Your turn: create a binary variable of 0 and 1 called loc_risk_binary
# that converts M1_Location_risk so "High Risk" = 1 and any other value = 0
skc["loc_risk_binary"] = (skc["M1_Location_risk"]=="High Risk").astype(int)
skc["loc_risk_binary"]
#Logistic regression model
loc_race_logreg = logit("loc_risk_binary ~ Race_binary", data=skc).fit()
loc_race_logreg.summary()

loc_race_logreg.params

loc_race_logreg_OR = np.exp(loc_race_logreg.params)
#Recode the logistic regression model so the reference level is White
####

#Module 10 covers risk ratios, fisher's exact and other hypothesis tests (look out for video this weekend)

#------------- Multiple Logistic Regression Model with Forest Plot -----------------
loc_race_mlogreg = logit("loc_risk_binary ~ C(Race_binary, Treatment(reference='White')) +"
                         "Age + Gender", data = skc).fit()
loc_race_mlogreg.summary()
#Your turn: exponentiate the parameters to get the ORs
loc_race_mlogreg.params
loc_race_mlogreg_OR = np.exp(loc_race_mlogreg.params); print(loc_race_mlogreg_OR)

#---------------------------------------------------------------
# Forest Plot
#---------------------------------------------------------------
params = loc_race_mlogreg.params
conf = loc_race_mlogreg.conf_int()
or_df = pd.DataFrame({
    "OR": np.exp(params),
    "CI_lower": np.exp(conf[0]),
    "CI_upper": np.exp(conf[1])
})
# Drop intercept (not useful in forest plot)
or_df = or_df.drop("Intercept") #drop the intercept row
print(or_df)

#------Create forest plot-------
or_df = or_df.sort_values("OR", ascending= True) #sort the coeffcients based on OR
or_df.index = ["POC", "Gender", "Age"]
plt.figure()
plt.errorbar(
    x=or_df["OR"],
    y=or_df.index,
    xerr=[or_df["OR"] - or_df["CI_lower"],
          or_df["CI_upper"] - or_df["OR"]],
    fmt='o') #draw each estimate as a circle (dot))
plt.axvline(1, linestyle='--')  # no-effect line
plt.xscale('log')  #important! The log scale ensures visual symmetry. OR = .5 and OR=2 will look the same distance away from 1
#ax = plt.gca()
#ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
plt.xlabel("Odds Ratio")
plt.title("Forest Plot (Logistic Regression)")
plt.tight_layout()
plt.show()

#Also a built in package called forestplot as fp