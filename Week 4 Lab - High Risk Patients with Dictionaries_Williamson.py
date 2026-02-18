#Create a dictionary of patients from the 2 lists. Add their symptoms to this dictionary
patients = [
    ["Alice", ["fever", "cough"]],
    ["Bob", ["fever", "shortness of breath"]],
    ["Charlie", ["rash", "fever"]],
    ["David", ["fatigue"]],
    ["Eva", ["fever", "cough", "shortness of breath"]],
    ["Frank", ["headache", "fatigue"]],
    ["Grace", ["sore throat"]],
]

#symptoms = [patient[1] for patient in patients]; print(symptoms)
#Write the for loop version of this list comprehension

# Initialize empty list to store diagnoses
patient_diagnosis = []

# Loop through each patient (this is one way to write a for loop)
for patient in patients:
    name = patient[0]  # Extract patient name
    symptoms = patient[1]  # Extract symptom list
    # Determine diagnoses using if-elif-else conditional tests
    if ("fever" in symptoms) and ("cough" in symptoms): #Note: if "fever" and "cough" in symptoms is not correct.
        diagnosis = "Possible Flu"
    elif ("fever" in symptoms) and ("shortness of breath" in symptoms):
        diagnosis = "Possible COVID-19"
    elif ("rash" in symptoms) and ("fever" in symptoms):
        diagnosis = "Possible Measles"
    elif ("fatigue" in symptoms) and ("fever" not in symptoms):
        diagnosis = "Possible Anemia"
    elif ("headache" in symptoms) or ("fatigue" in symptoms):
        diagnosis = "Possible Dehydration or Stress"
    else:
        diagnosis = "No clear diagnosis"

    # Append diagnosis in a list with the patient name and their symptoms
    patient_diagnosis.append([name, symptoms, diagnosis])

    # Print patient name, symptoms and diagnosis for each patient
    print(f"Patient: {name}")
    print(f"  Symptoms: {', '.join(symptoms)}")
    print(f"  Diagnosis: {diagnosis}\n")
    # \n ensures that a line is skipped before the next patient's information and diagnosis is printed



