#===========================================================================================================
# This file reads in and cleans the PTSD data and preps the dataset for Data Analysis
#===========================================================================================================
#-----------------------------------------------------------------------------------------------------------
#IMPORT MODULES, OPEN AND INSPECT DATA
#-----------------------------------------------------------------------------------------------------------
import pandas as pd
import os
from tableone import TableOne

print(os.getcwd()) #get current working directory
os.chdir(r'C:\\Users\\Najiy\\OneDrive\\Desktop\\PycharmProjects\\BIOS584-Python') #set working directory

#Read from an excel file - this filepath will give you an error in windows only (not with Macs or Linux)
#df = pd.read_excel("C:\Users\lylae\PycharmProjects\PTSD_DataAnalysis\PTSD_data_excel.xlsx") #will give error
#Python interprets \U (like in \Users) as a Unicode escape sequence, which leads to errors like \UXXXXXXXX.
#Ways to fix this error: forward slashes /, double backslashes \\ or telling Python it's a raw string r"your path name"
ptsd = pd.read_excel(r"Week 8 PTSD Analysis\RealPTSD_data_excel-1-1.xlsx") #easiest way
ptsd = pd.read_excel(r'Week 8 PTSD Analysis/RealPTSD_data_excel-1-1.xlsx',
        na_values=["???", "-99", -99, "999", 999])
#-------------------------------------------------------------
#Inspect data
#-------------------------------------------------------------
print(ptsd); print(ptsd.head(10)) #483 rows, 439 columns; print first 10 rows
print(ptsd.info()) #structure of dataframe: 483 rows, 439 columns
print(ptsd.columns) #column names
print(ptsd.describe()) #summary statistics of numeric columns, need to change categorical vars with numeric values
print(ptsd.describe().iloc[:, 50:100]) #iloc is locating by the index
#ptsd.describe()[['col1', 'col2', 'col3']]
pd.set_option('display.width',15) #control how many columns to show (this shows 15 columns)
print(ptsd.describe())
pd.set_option('display.max_columns', None) #None means show all columns
print(ptsd.describe())
#Reset to default settings
pd.reset_option('display.max_columns')
pd.reset_option('display.width')

ptsd["gender_code"].value_counts() #how to see the counts for categorical variables

#-------------------------------------------------------------
# Check missing data
#-------------------------------------------------------------
print(ptsd.isnull().sum()) #counts up missing values for each column
print(ptsd.isnull().sum(axis=1)) #counts up missing values for each ROW
#Usually you would fill missing data here, if needed (datacamp will teach you how)

#-----------------------------------------------------------------------------------------------------------
# DATA PREP FOR EDA
#-----------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------
# Create new dataframe with informative categorical variables
#-------------------------------------------------------------
# Dictionary of dictionaries (what each category should map to for all categorical columns of interest)
cat_maps = {
    "gender_code": {
        1: "Male",
        2: "Female"
    },
    "race_code": {
        1: "White",
        2: "African American",
        3: "Asian/Pacific Islander",
        4: "Native American",
        5: "Multi-racial",
        6: "Missing"
    },
    "ethnicity_code": {
        1: "Hispanic/Latino",
        2: "Non-Hispanic",
        3: "Missing"
    },
    "sexualorient_code": {
        1: "Heterosexual",
        2: "LGBTQ+Identifying",
        3: "Other/Missing/Not Reported"
    },
    "education_code": {
        1: "Less than Bachelor's",
        2: "Bachelor's or Higher",
        3: "Missing or Not Reported"
    },
    "employment_code": {
        1: "Employed",
        2: "Unemployed",
        3: "Retired",
        4: "Disabled/Unable to Work",
        5: "Student",
        6: "Missing or Not Reported"
    },
    "rank_code": {
        1: "Enlisted (E1-9)",
        2: "Officer (WO2-5, O2-6)",
        3: "Missing or Not Reported"
    },
    "sexual_trauma": {
        0: "No",
        1: "Yes"
    }

}

#Create NEW dataframe with replaced categorical variables
ptsd_cat = ptsd.replace(cat_maps, inplace=False) #inplace=False, creates a copy of the dataset
print(ptsd_cat["gender_code"]) #check that it worked
#ptsd.replace(cat_dict, inplace=True) #inplace=True would modify the dataframe directly
# useful if you have a large dataframe and don't want to waste memory keeping an old version


#----------------------------------------------------
# Subset data to variables of interest for EDA
#----------------------------------------------------
print(ptsd_cat["record_id"])
print(ptsd_cat[["record_id", "ptsdpresent_caps"]]) #extract 2 columns
print(ptsd_cat[ptsd_cat.columns[:15]]) #extract the first 15 columns

# Select variables for your table (create a list with those variable names)
table1_vars = [
    "age_iop", "gender_code", "sexualorient_code", "race_code", "ethnicity_code",
    "education_code", "employment_code", "rank_code",
    "caps_intake", "pcl5_score_intake",  "phq9_score_intake",
    "ctq_total_score","sud_code","branch_code",
    "mdd_code","sexual_trauma"
]
#subsetted dataframe
table1_df = ptsd_cat[table1_vars]; print(table1_df)

#-----------------------------------------------------------------------------------------------------------
# Save clean dataset to Excel or CSV
#-----------------------------------------------------------------------------------------------------------
table1_df.to_excel("table1_df.xlsx", index=False) #index = False avoids writing row numbers as a column
#df_cleaned.to_csv("cleaned_data.csv", index=False)

#-----------------------------------------------------------------------------------------------------------
# CREATE TABLE 1 OF SUMMARY STATISTICS FOR DEMOGRAPHIC VARIABLES
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------
# Define categorical and continuous variables
#-----------------------------------------------------------
categorical_vars = [
    "gender_code", "sexualorient_code", "race_code", "ethnicity_code",
    "education_code", "employment_code", "rank_code", "sud_code","branch_code",
    "mdd_code","sexual_trauma"]

continuous_vars = [
    "age_iop", "caps_intake", "pcl5_score_intake", "ctq_total_score", "phq9_score_intake"]


#-----------------------------------------------------------
# Create Table 1 Summary Statistics
#-----------------------------------------------------------
table1 = TableOne(data=table1_df,
                  columns=categorical_vars + continuous_vars,
                  categorical = categorical_vars,
                  groupby=None,  # you can group if needed, e.g., by gender
                  pval=False)

# Print summary
print(table1.tabulate(tablefmt="grid", floatfmt=".2f"))








#-----------------------------------------------------------------------------------------------------------
#FOR YOUR REFERENCE: how to change the data type of columns (say the integers in a cat var should be strings)
#-----------------------------------------------------------------------------------------------------------
# Convert all categorical variables of interest to string data
columns_to_convert = [
    "gender_code", "sexualorient_code", "race_code", "ethnicity_code",
    "education_code", "employment_code", "rank_code"
]
ptsd.loc[:, columns_to_convert] = ptsd[columns_to_convert].astype(str)
#The : means "all rows", and "columns_to_convert" specifies the columns

#Another way to change the data types of variables
ptsd = ptsd.astype({
    "age_iop": "int32", #integer but less memory needed than int64 (It uses 32 bits of memory to store the number)
    "gender_code": "str"
})

#Later you can extract all your categorical variables by extracting columns of a certain datatype (not int or floats)
cat_vars = ptsd.select_dtypes(include=["object", "string"])
print(cat_vars)

