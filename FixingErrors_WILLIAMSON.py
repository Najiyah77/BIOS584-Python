#-----------------------------------------------------------------------
# Application 4: Identifying and Fixing Incorrect Code
# Name: Najiyah Williamson
# Due Date: 2/27/26
#-----------------------------------------------------------------------

'''
# peer code
patients = ["Alice", "Bob", "Charlie", "David", "Ted", "Sam", "Jennifer", "Tom"]
glucose_levels = [140, 155, 130, 180, 200, 260, 220, 190]
high_glu_patients = []

#i in the current for loop represents a string, not an index. To fix, using a range(len(patients)).
for i in patients:
    #the following statement will not work unless i is fixed
    if glucose_levels[i] >= 200:
    #this print statement will not work because i is not an index yet.
        print(f"{patients[i]}, you have a high glucose level of {
                glucose_levels[i]}.")
    #append should only take one argument, not two. so remove the patients[i]. Also you should not reassign high_glu_patients becuase it will return None. It will break the code. Remove the "high_glu_patients ="
    high_glu_patients = high_glu_patients.append(patients[i],
        glucose_levels[i])

# there is a typo in 'high_glu_patient'. There should be an s after the t in patient there.
glucose_avg = sum(high_glu_patient) / len(high_glu_patients)

#this will print only the number for the glucose average. Will need to be print(f"Average High Glucose Level: {glucose_avg:.2f}")
print(glucose_avg)
'''

# corrected code
patients = ["Alice", "Bob", "Charlie", "David", "Ted", "Sam", "Jennifer", "Tom"]
glucose_levels = [140, 155, 130, 180, 200, 260, 220, 190]
high_glu_patients = []

for i in range(len(patients)):
    if glucose_levels[i] >= 200:
        print(f"{patients[i]}, you have a high glucose level of {
                glucose_levels[i]}.")
        high_glu_patients.append(glucose_levels[i])

glucose_avg = sum(high_glu_patients) / len(high_glu_patients)
print(f"Average High Glucose Level: {glucose_avg:.2f}")
