#---------------------------------------------------------------
# Module 6 Exercises using lists vs using Numpy arrays
# Name:
# Date:
#---------------------------------------------------------------
import numpy as np

#----------------------------------------------------------------
#An example of vectorized operations in numpy vs iterative operations in lists
#Goal: add 10 to each item
#----------------------------------------------------------------
#Arrays have element-wise, vectorized operations:
#can apply a math function to all elements at once
array = np.array([10, 12, 8, 15])
new_array = array + 10
print(new_array)

#Lists can only do iterative operations (this is a slower process)
list1 = [10, 12, 8, 15]
new_list = []
for number in list1:
    new_list.append(number + 10)
print(new_list)

#List comprehension version of the same for loop
new_list_lc = [number + 10 for number in list1]
print(new_list_lc)

#---------------------------------------------------------
# Exercise 1: Disease Surveillance:average daily cases & peak day
#---------------------------------------------------------

#----------- Exercise 1 with lists -----------
# Daily cases (number of people who got a disease each day in a week)
cases_list = [3, 5, 2, 8, 4, 6, 1] #7 days of cases

# To get average, need to get sum and divide by total days (len of the list)
mean_cases = sum(cases_list)/len(cases_list)

# Find max number of cases & identify day with the max number of cases (argmax)
max_val = max(cases_list)
for i in range(1, len(cases_list)):
    if cases_list[i] == max_val:
        max_day = i

#An equivalent for loop to do this
for index, case in enumerate(cases_list):
    if case == max_val:
        max_day = index

print(f"Total cases in week: {total}")
print(f"Average cases/day: {mean_cases:.2f}")
print(f"Max cases/day: {max_day:.2f}")
print(f"Day with maximum cases: {max_day}")

    #----------- Exercise 1 with Numpy arrays -----------
import numpy as np
cases_array = np.array(cases_list)

#With numpy arrays, I can do the above tasks with no for loops!
cases_array.sum()
cases_array.mean()
cases_array.max()
cases_array.argmax() #position in array that has the max value

#If I want to print it with f strings
print(f"Total cases in week: {cases_array.sum()}")
print(f"Average cases/day: {cases_array.mean():.2f}")
print(f"Max cases/day: {cases_array.max():.2f}")
print(f"Day with maximum cases: {cases_array.argmax()}")

#---------------------------------------------------------
# Exercise 2: Disease rates per 100,000 people in 4 towns
#---------------------------------------------------------

#----------- Exercise 2 with Numpy arrays -----------
# Illustrates that Numpy has element-wise and vectorized operations
# Vectorized math = can apply a math function to all elements at once
cases = np.array([10, 12, 8, 15]) #Number of disease cases in each of the 4 towns
population = np.array([5000, 8000, 4000, 10000]) #Population of 4 towns
rate_per_100k = (cases / population) * 100000 #returns array of 4 rates/100K people
print(rate_per_100k)

#----------- Exercise 2 with Lists -----------
#Have to iterate manually element by element, no vectorized operations
cases_list = [10, 12, 8, 15] #Number of disease cases in each of the 4 towns
pop_list = [5000, 8000, 4000, 10000]  #Population of 4 towns

rate_per_100k_list = []
for cases, pop in zip(cases_list, pop_list):
    rate_per_100k = (cases / pop) * 100_000
    rate_per_100k_list.append(rate_per_100k)
print(rate_per_100k_list)


#---------------------------------------------------------
# Exercise 3: Identifying Flint MI homes with dangerous lead levels
#--------------------------------------------------------

#----------- Exercise 3 with Lists -----------
# List of lead levels (ppb) for 73 Flint, MI homes
lead_levels_list = [
    3, 5, 2, 18, 4, 16, 1, 7, 9, 12,
    14, 20, 6, 8, 11, 15, 17, 10, 13, 19,
    21, 4, 2, 6, 18, 23, 5, 7, 9, 16,
    12, 14, 3, 1, 22, 24, 8, 10, 11, 13,
    15, 17, 19, 20, 6, 4, 2, 18, 21, 23,
    25, 7, 9, 12, 14, 16, 5, 3, 1, 8,
    10, 11, 13, 15, 17, 19, 20, 22, 24, 6,
    4, 2, 18]
danger_threshold = 15  # EPA action level (ppb). Lead levels > 15 = dangerous

dangerous_homes = []
dangerous_levels = []
for home_id, lead_ppb in enumerate(lead_levels_list):
    if lead_ppb >= danger_threshold:
        dangerous_homes.append(home_id)
        dangerous_levels.append(lead_ppb)

#Number of dangerous homes and average lead level among dangerous homes
num_dangerous_homes = len(dangerous_homes)
avg_dangerous_level = sum(dangerous_levels) / num_dangerous_homes if num_dangerous_homes > 0 else 0

print("Dangerous home IDs:", dangerous_homes)
print("Number of dangerous homes:", num_dangerous_homes)
print("Lead levels in dangerous homes (ppb):", dangerous_levels)
print("Average lead level among dangerous homes (ppb):", round(avg_dangerous_level, 2))

#---------- Exercise 3 with Numpy arrays -----------
lead_levels_list = [
    3, 5, 2, 18, 4, 16, 1, 7, 9, 12,
    14, 20, 6, 8, 11, 15, 17, 10, 13, 19,
    21, 4, 2, 6, 18, 23, 5, 7, 9, 16,
    12, 14, 3, 1, 22, 24, 8, 10, 11, 13,
    15, 17, 19, 20, 6, 4, 2, 18, 21, 23,
    25, 7, 9, 12, 14, 16, 5, 3, 1, 8,
    10, 11, 13, 15, 17, 19, 20, 22, 24, 6,
    4, 2, 18]
lead_levels_array = np.array(lead_levels_list)
danger_threshold = 15  # EPA action level (ppb). Lead levels > 15 = dangerous

lead_danger_status = lead_levels_array >= danger_threshold #returns boolean numpy array of True/Falses
num_dangerous = lead_danger_status.sum() #Sums up all True's. True = 1 in Python
dangerous_homes = np.where(lead_danger_status)[0] #which homes have lead_danger_status as marked True?
#Alternative: dangerous_homes = np.where(lead_levels_array >= danger_threshold)[0]
#Another use of np.where: np.where(condition, value_if_true, value_if_false)
np.where(lead_levels_array >= danger_threshold, "Unsafe", "Safe")

dangerous_levels = lead_levels_array[dangerous_homes] #subset = get array with the lead levels of only dangerous homes
#Alternative way to subset: use boolean array
#             dangerous_levels = lead_levels_array[lead_danger_status]
#             #extracts lead levels where lead_danger_status is true. lead_danger_status == True is implied
avg_dangerous_level = dangerous_levels.mean() if num_dangerous > 0 else 0
safe_levels = lead_levels_array[lead_danger_status==False]

print("Number of dangerous homes out of 73 in sample:", num_dangerous)
print("Dangerous home IDs:", dangerous_homes)
print("Lead levels in dangerous homes (ppb):", dangerous_levels)
print("Average lead level among dangerous homes (ppb):", round(avg_dangerous_level, 2))
