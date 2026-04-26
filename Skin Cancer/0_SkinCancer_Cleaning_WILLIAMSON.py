#---------------------------------------------------------------------------------------
# This file cleans and preps the Skin Cancer data for analysis
#------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Set working directory
print(os.getcwd()) #get current working directory
os.chdir(r'C:\Users\Najiy\OneDrive\Desktop\PycharmProjects\BIOS584-Python\Skin Cancer') #set working directory (change it to your filename)

#Read in data
df = pd.read_excel("skin_cancer.xlsx")

#-----Explore data-----
df.info()
df.columns
df.head() #default is 5 rows

#-----Subset data to columns of interest-----
subset_vars = ["Age", "Gender","M1_Location_risk","cancer_type","immuno_none",
               "num_primary_malignancies","prior_skin_cancer","Racial Identity",
               "m1_time_to_diagnosis"]
skc_df = df[subset_vars].copy() #equivalent to df.loc[:, subset_vars]

#-----Clean data-----
skc_df["Racial Identity"].value_counts()
skc_df["Racial Identity"] = skc_df["Racial Identity"].str.strip().str.title() #getting rid of any spaces, and fixing spelling
skc_df["Racial Identity"].value_counts() # double checking

#Dictionary of dictionaries telling us how to map the categorical labels
cat_maps = { #you finish Racial Identity mapping
    "Racial Identity": {
        "Black Or African American": "Black",
        "Caucasian": "White",
        "Asian": "Other",
        "Hispanic": "Other"

    },
    "Gender": {
        "M": "Male",
        "F": "Female"
    },
    "immuno_none": {
        1: "Not immunocompromised",
        0: "Immunocompromised"
    },
    "M1_Location_risk": {
        "Area H": "High Risk",
        "Area M": "Medium Risk",
        "Area L": "Low Risk"
    }

}

#replace labels in categorical variables as specified in cat_maps
skc_df = skc_df.replace(cat_maps)

#alternatively can write skc_df.replace(cat_maps, inplace=True) with no variable assignment (object mutation)
#Check that the mapping worked
skc_df["Gender"]
skc_df["Racial Identity"].value_counts()
skc_df["Racial Identity"].value_counts(normalize=True)*100 #percentages

#-----Create binary variables-----
#Create new POC variable that is 0 and 1s - so getting dummy variables
skc_df["POC"] = (skc_df["Racial Identity"]!="White").astype(int) # not white is 1, white is 0
skc_df["POC"]
#Now do it for prior skin cancer history -> change No to 0, Yes to 1. Don't create new variable
skc_df["prior_skin_cancer"] = (skc_df["prior_skin_cancer"]=="Yes").astype(int)
skc_df["prior_skin_cancer"] #check that it worked

#Create new binary race variable called "Race_binary" with White and POC labels
skc_df["Race_binary"] = np.where(skc_df["Racial Identity"] == "White", "White", "POC") # where it is white, make it white, if else then do POC
skc_df["Race_binary"]
#Your turn: Transform "num_primary_malignancies" into a new variable called num_cancers_binary
# that has values "One cancer" or "More than one cancer"
skc_df["num_primary_malignancies"] = np.where(skc_df["num_primary_malignancies"]==1, "One cancer", "More than one cancer")
skc_df["num_primary_malignancies"]

#----- Identify missing data and remove missing data ----
skc_df.isna().sum() # tells me for evey variable, how many missing values there were
#skc_df = skc_df.dropna() drops rows if ANY column has missing values, sometimes might be aggressive
skc_df_cc = skc_df.dropna(subset = ["m1_time_to_diagnosis"]) #drop rows where m1_time_to_diagnosis has missing info
skc_df_cc.isna().sum()

#Save cleaned data with no missing values
skc_df.to_excel("cleaned_skc.xlsx")
skc_df_cc.to_excel("cleaned_skc_cc.xlsx")

