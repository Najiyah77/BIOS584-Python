#-------------------------------------------------------------------
# Week 4 Lab - Identifying High Risk Patients with Dictionaries
# Name: Najiyah Williamson
# Date: 02/18/26
# Hint: See Chapter 6 and Module 4 Notes
#-------------------------------------------------------------------
patient_names = ["Alice", "Bob", "Charlie", "David", "Ted", "Sam", "Jennifer", "Tom", "Grace","Frank"]
glucose_levels = [140, 155, 130, 180, 200, 160, 120, 190, 260, 300]

#Create a dictionary from the 2 lists above with patient names as the keys
# and glucose_levels as the values. Use zip()
patients_dict = dict(zip(patient_names, glucose_levels))
print(patients_dict)

#Write a for loop that iterates through the items of the dictionary, identifies
# patients who have glucose levels greater than 150 and adds those
# patients (names and their glucose levels) to a list called "high risk patients".
high_risk_patients = []
for name, glucose in patients_dict.items():
    if glucose > 150:
        high_risk_patients.append([name, glucose])

#Write a list comprehension version of the for loop that loops through the dictionary items
high_risk_patients = [[name, glucose] for name, glucose in patients_dict.items() if glucose > 150]

#Print out a message to each high risk patient:
# "Hey [name], your glucose level is [fill in their glucose level]. You are at
# high risk for diabetes!"
for name, glucose in high_risk_patients:
    print(f"Hey {name}, your glucose level is {glucose}. You are at high risk for diabetes!")