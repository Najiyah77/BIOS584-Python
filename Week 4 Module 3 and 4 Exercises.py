
#---------------------------------------------------
# Application: Filtering patients with High Diabetes Risk
# Name: Najiyah Williamson
# Date: 02/13/26
#---------------------------------------------------
patient_names = ["Alice", "Bob", "Charlie", "David", "Ted", "Sam", "Jennifer", "Tom"]
glucose_levels = [140, 155, 130, 180, 200, 160, 120, 190]

#---------------------Method 1---------------------
#Create list of high risk patient names with their levels
high_risk_patients = []

#Loop through glucose_levels and identify if a person's level is greater than 150
for i in range(len(patient_names)):
    if glucose_levels[i] >= 150: # If greater than 150, add the person's name and glucose level to "high risk patients" list
        high_risk_patients.append((glucose_levels[i], patient_names[i]))

#Sort the patients from highest to lowest risk and print
high_risk_patients.sort(reverse=True)
#THIS IS VALID: high_risk_patients = sorted(high_risk_patients, reverse=True)
#WRONG: high_risk_patients = high_risk_patients.sort(reverse=True)

#---------------------Method 2: List comprehensions---------------------
high_risk_patients = sorted([[glucose_levels[i], patient_names[i]] for i in range(len(patient_names))
                        if glucose_levels[i] > 150], reverse=True)
print(high_risk_patients)

#---------------------Method 3: enumerate() for loop ---------------------
high_risk_patients = []
for index, glucose in enumerate(glucose_levels):
    if glucose > 150:
        high_risk_patients.append((glucose, patient_names[index]))

#List comprehension exercise - convert the enumerate for loop into a list comprehension
high_risk_patients = [[glucose, patient_names[index]] for index, glucose in enumerate(glucose_levels) if glucose > 150]

high_risk_patients.sort(reverse=True)
print(high_risk_patients)

#---------------------Method 4: zip() function ---------------------
high_risk_patients = []
for glucose, name in zip(glucose_levels, patient_names): #pairing up each item to create a sequence of each pairwise combination. glucose refers to first item (glucose_levels) and then name to patient_names)
    if glucose > 150:
        high_risk_patients.append((glucose, name))

high_risk_patients.sort(reverse=True)
print(high_risk_patients)

#List comprehension exercise - convert the zip() for loop into a list comprehension
high_risk_patients = sorted([[glucose, name] for glucose, name in zip(glucose_levels, patient_names) if glucose > 150], reverse=True)
print(high_risk_patients)

#Creating combined list with zip() - creates a list of tuples
patient_data = list(zip(glucose_levels, patient_names))
print(patient_data)

# Create a dictionary from the 2 lists with zip()
patients_dict = dict(zip(patient_names, glucose_levels))
print(patients_dict)

#-------------------- Method 5: enumerate()---------------------


#------------------------------------------------------------------------------
# Application with dictionaries
#------------------------------------------------------------------------------
patient_names = ["Alice", "Bob", "Charlie", "David", "Ted", "Sam", "Jennifer", "Tom"]
glucose_levels = [140, 155, 130, 180, 200, 160, 120, 190]

patients_dict = {"Alice":140, "Bob":155, "Charlie": 130, "David": 180,
                 "Ted":200, "Sam": 160, "Jennifer": 120, "Tom":190}



#-------------------- Dictionary Method 2 using zip()----------------------

