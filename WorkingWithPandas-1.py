#=======================================================================================================================
# This python script shows the basic attributes of pandas dataframes and reads in data from a CSV file
# BIOS 584 Module 8
#=======================================================================================================================
#Importing necessary packages
import pandas as pd
import numpy as np
import os #accessing operating system to get/set working directory, install packages, etc.

os.getcwd()

#-----------------------------------------------------------------------------------------------------------------------
# Creating and inspecting a pandas data frame
#-----------------------------------------------------------------------------------------------------------------------
""" A pandas dataframe is similar to a dictionary of arrays (technically called a "pandas series") with some 
other properties like all the arrays need to be the same length and each array can have a label)! 
The "Keys" are the column names (aka the variables) and the "values" are a labeled numpy array of the observations 
(aka the rows in a dataset). Each array can have a label (aka a row name, which is usually just the row number).
Note: a numpy array (has to have homogenous data - each element must be the same type) is just a list 
but with vectorized operations and methods for fast math operations. """
#--------------------------------------------------------------------------------------
# Converting a dictionary to a pandas dataframe
#--------------------------------------------------------------------------------------
# Dictionary with column names as keys
data_dic = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'is_student': [False, True, False]
}
# Create DataFrame by converting a dictionary
df = pd.DataFrame(data_dic)
# Display the DataFrame
print(df)
#Why don't we always use pandas dataframes? Why use dictionaries at all?

#--------------------------------------------------------------------------------------
# Creating a pandas dataframe from scratch and inspecting it
#--------------------------------------------------------------------------------------
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', "David"],
    'A': [1, 2, 3, 4],
    'B': [2, 3, 4,5],
})
print(df) #displays the whole thing
print(df['A']) #extract the obs in col A (same syntax as looking up the value of a key in a dictionary!dict["key"])
print(df.head()) #displays the first 5 rows
print(df.tail()) #displays the last 5 rows

#3 components of a pandas dataframe
print(df.values) #2D numpy array of all the observations
print(df.columns) #column names
print(df.index) #row labels (usually the row numbers/indices unless you specify the labels of rows)

df.index = ['Person 1', 'Person 2', 'Person 3', 'Person 4'] #changing the row labels or the "index" of the dataframe
print(df)
df.loc["Person 1"] #row labels are helpful because you can extract ALL the observations in a row across columns
#Same syntax as dict["key"] or df["column name"] but you add ".loc"

# Set the "name" column as the index of the dataframe (row labels)
#Note: data frames are mutable! So let's first create a copy of the dataframe OBJECT
df_named = df.copy() #now changes to df_copy will not affect original df
#df_copy = df #what NOT to do, this line creates another reference to the same df object
df2 = df
#any changes to df2 will also change df


df_named = df_named.set_index("name")
print(df_named)
df_named.loc["Alice"] #Alternative is df[df["name"] == "Alice"] but df.loc is faster O(1) lookup


print(df.describe()) #summary statistics for numeric columns (floats or ints)
print(df.info()) #like str() in R, returns the data frame's structure


