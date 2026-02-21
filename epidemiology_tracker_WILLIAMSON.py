#-----------------------------------------------------------------------
# Application 1: Epidemiology Metric Report Generator
# Name: Najiyah Williamson
# Due Date: 2/27/26
#-----------------------------------------------------------------------

#COLLECTING USER INPUT with CLEANING AND VALIDATION
# city name (correcting improper capitalization and remove extra spaces)
city = input("Enter the city name: ").strip().title()
city = " ".join(city.split())

while not city.replace(" ", "").isalpha():
    print("Please enter a valid city name with letters.")
    city = input("Enter the city name: ").strip().title()

# disease name
disease = input("Enter the disease name: ").strip().title()
disease = " ".join(disease.split())

while not disease.replace(" ", "").isalpha():
    print("Please enter a valid disease name with letters.")
    disease = input("Enter the disease name: ").strip().title()

# total population of the city (number with no commas)
totpop = input("Enter the total population: ").strip()

while not totpop.isdigit() or int(totpop) <= 0:
    print("Invalid input. Enter a positive whole number with no commas.")
    totpop = input("Enter the total population: ").strip()

totpop = int(totpop)

# number of reported cases (number with no commas)
reported_cases = input("Enter the number of reported cases: ").strip()

while not reported_cases.isdigit() or int(reported_cases) <= 0:
    print("Invalid input. Enter a positive whole number with no commas.")
    reported_cases = input("Enter the number of reported cases: ").strip()

reported_cases = int(reported_cases)

# number of deaths (number with no commas)
deaths = input("Enter the number of deaths: ").strip()

while not deaths.isdigit():
    print("Invalid input. Enter a positive whole number with no commas.")
    deaths = input("Enter the number of deaths: ").strip()

deaths = int(deaths)

# number of true positive cases
true_pos_cases = input("Enter the number of true positive cases: ").strip()

while not true_pos_cases.isdigit():
    print("Invalid input. Enter a positive whole number with no commas.")
    true_pos_cases = input("Enter the number of true positive cases: ").strip()

true_pos_cases = int(true_pos_cases)

# number of false negative cases
false_neg_cases = input("Enter the number of false negative cases: ").strip()

while not false_neg_cases.isdigit():
    print("Invalid input. Enter a positive whole number with no commas.")
    false_neg_cases = input("Enter the number of false negative cases: ").strip()

false_neg_cases = int(false_neg_cases)

# number of true negative cases
true_neg_cases = input("Enter the number of true negative cases: ").strip()

while not true_neg_cases.isdigit():
    print("Invalid input. Enter a positive whole number with no commas.")
    true_neg_cases = input("Enter the number of true negative cases: ").strip()

true_neg_cases = int(true_neg_cases)

# number of false positive cases
false_pos_cases = input("Enter the number of false positive cases: ").strip()

while not false_pos_cases.isdigit():
    print("Invalid input. Enter a positive whole number with no commas.")
    false_pos_cases = input("Enter the number of false positive cases: ").strip()

false_pos_cases = int(false_pos_cases)

#EPIDEMIOLOGICAL CALCULATIONS
prevalence = (reported_cases / totpop) * 100
case_fatality_rate = (deaths / reported_cases) * 100
mortality_rate = (deaths / totpop) * 100

sensitivity = (true_pos_cases / (true_pos_cases + false_neg_cases)) * 100
specificity = (true_neg_cases / (true_neg_cases + false_pos_cases)) * 100

pos_pre_value = (true_pos_cases / (true_pos_cases + false_pos_cases)) * 100
neg_pre_value = (true_neg_cases / (true_neg_cases + false_neg_cases)) * 100

#FORMATTED EPIDEMIOLOGY REPORT
print(
    "Epidemiology Report:\n"
    "----------------------------------------------\n"
    f"City: {city}\n"
    f"Disease: {disease}\n"
    f"Population: {totpop:,}\n"
    f"Cases: {reported_cases:,}\n"
    f"Deaths: {deaths:,}\n"
    "\n"
    f"\tPrevalence: {prevalence:.3f}%\n"
    f"\tCase Fatality Rate: {case_fatality_rate:.3f}%\n"
    f"\tMortality Rate: {mortality_rate:.3f}%\n"
    "\n"
    "Diagnostic Test Performance:\n"
    f"\tSensitivity: {sensitivity:.3f}%\n"
    f"\tSpecificity: {specificity:.3f}%\n"
    f"\tPositive Predictive Value: {pos_pre_value:.3f}%\n"
    f"\tNegative Predictive Value: {neg_pre_value:.3f}%\n"
    "\n"
    "Summary:\n"
    f"The prevalence of {disease} in {city} is {prevalence:.3f}%.\n"
    f"The case fatality rate is {case_fatality_rate:.3f}%.\n"
    f"Testing sensitivity is {sensitivity:.3f}%.\n"
)
