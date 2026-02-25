#------------------------------------------------
# Week 5 Lab
# Name: Najiyah Williamson
# Date: 2/25/26
#------------------------------------------------
#WATCH THE LAB VIDEO AND CODE ALONG WITH ME

patients = [
    ["Alice", ["fever", "cough"],140],
    ["Bob", ["fever", "shortness of breath"],155],
    ["Charlie", ["rash", "fever"],130],
    ["David", ["fatigue"],200],
    ["Eva", ["fever", "cough", "shortness of breath"],180],
    ["Frank", ["headache", "fatigue"],200],
    ["Grace", ["sore throat"],120],
]


#------------------ EXERCISE 1 -------------------
#EXERCISE: Using a FOR LOOP, create a dictionary called "patient_info"
# using the nested list above and print the dictionary. The names should be keys and the values
#should be another dictionary. Example of the first 2 items in the dictionary:
# {"Alice": {"Symptoms": ["fever","cough"], "Glucose Level": 140}
#  "Bob": {"Symptoms": ["fever", "shortness of breath"], "Glucose Level": 155}
# }
patients_info = {}

for patient in patients:
    name = patient[0]; symptoms = patient[1]; glucose_level = patient[2] #index
    patients_info[name] = {"Symptoms": symptoms, "Glucose Level": glucose_level}

print(patients_info)


#EXERCISE: Retrieve and print Bob's symptoms from the patient info dictionary
print(patients_info["Bob"]["Symptoms"])


#------------------ EXERCISE 2 -------------------
patients = [
    ["Alice", ["fever", "cough"]],
    ["Bob", ["fever", "shortness of breath"]],
    ["Charlie", ["rash", "fever"]],
    ["David", ["fatigue"]],
    ["Eva", ["fever", "cough", "shortness of breath"]],
    ["Frank", ["headache", "fatigue"]],
    ["Grace", ["sore throat"]],
]
glucose_levels = [140, 155, 130, 180, 200, 160, 120]

#zip(patients, glucose_levels) --> (["Alice", ["fever", "cough"]], 140), (["Bob", ["fever", "shortness of breath"]],155)
#EXERCISE: Using a zip() for loop, create and print a dictionary of all patient info using the 2 lists above
patients_info = {}
for patient, glucose_level in zip(patients, glucose_levels):
    name = patient[0]; symptoms = patient[1]
    patients_info[name] = {"Symptoms": symptoms, "Glucose Level": glucose_level}
print(patients_info)


#EXERCISE: Retrieve and print Grace's glucose level from the patient info dictionary
print(patients_info["Grace"]["Glucose Level"])

#-------------------- Exercise 3 ------------------------
# EXERCISE:
# Loop through each patient in the patient dictionary
# to diagnose patients using the criteria below. Add the patient's diagnoses
# directly to the "patient_info" dictionary

#Example for Alice and Bob:
# {"Alice": {"Symptoms": ["fever","cough"], "Glucose Level": 140, "Diagnoses": ["Possible Flu"] }
#  "Bob": {"Symptoms": ["fever", "shortness of breath"], "Glucose Level": 155, "Diagnoses": ["Possible COVID-19"]}
# }

''' CRITERIA for Diagnoses:
fever and cough -> Possible Flu
fever and shortness of breath -> Possible COVID-19
rash and fever -> Possible Measles
fatigue and fever -> Possible Anemia 
headache and fatigue -> Possible Dehydration and Stress
No symptoms or not one of these conditions -> No clear diagnosis 
'''
for patient_name, patient_dict in patients_info.items():
    symptoms = patient_dict["Symptoms"] #extracted symptom list from patient dictionary
    diagnosis = []
    if ("fever" in symptoms) and ("cough" in symptoms):  # Note: if "fever" and "cough" in symptoms is not correct.
        diagnosis.append("Possible Flu")
    if ("fever" in symptoms) and ("shortness of breath" in symptoms):
        diagnosis.append("Possible COVID-19")
    if ("rash" in symptoms) and ("fever" in symptoms):
        diagnosis.append("Possible Measles")
    if ("fatigue" in symptoms) and ("fever" not in symptoms):
        diagnosis.append("Possible Anemia")
    if ("headache" in symptoms) or ("fatigue" in symptoms):
        diagnosis.append("Possible Dehydration or Stress")
    if diagnosis == []:
        diagnosis.append("No clear diagnosis")
    patient_dict["Diagnosis"] = diagnosis

print(patients_info)

#EXERCISE: Retrieve and print Eva's Diagnosis from the patient info dictionary
print(patients_info["Eva"]["Diagnosis"])

#-------------------- Exercise 4 --------------------
#EXERCISE: Print out the patient name, their symptoms and their diagnoses by looping through the
#patient info dictionary.
#Example output:
'''
Patient: Alice
    Symptoms: fever, cough
    Diagnosis: Possible Flu
    
Patient: Bob
    Symptoms: fever, shortness of breath
    Diagnosis: Possible COVID-19
    
... and so on for all patients
'''
for patient_name, patient_dict in patients_info.items():
    symptoms = patient_dict["Symptoms"] # extracting symptom list from patient dictionary
    diagnosis = patient_dict["Diagnosis"] # extract diagnosis list
    print(f"Patient: {patient_name}")
    print(f"    Symptoms: {", ".join(symptoms)}")
    print(f"    Diagnosis: {", ".join(diagnosis)}\n")
