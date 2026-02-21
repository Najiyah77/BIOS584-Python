import streamlit as st

st.title("Najiyah's Epidemiology Metric Report Generator")

#COLLECTING USER INPUT
# city name (correcting improper capitalization and remove extra spaces)
city = st.text_input("Enter the city name: ").strip().title()
city = " ".join(city.split())

# disease name
disease = st.text_input("Enter the disease name: ").strip().title()
disease = " ".join(disease.split())

# total population of the city (number with no commas)
totpop = st.text_input("Enter the total population: ").strip()

# number of reported cases (number with no commas)
reported_cases = st.text_input("Enter the number of reported cases: ").strip()

# number of deaths (number with no commas)
deaths = st.text_input("Enter the number of deaths: ").strip()

# number of true positive cases
true_pos_cases = st.text_input("Enter the number of true positive cases: ").strip()

# number of false negative cases
false_neg_cases = st.text_input("Enter the number of false negative cases: ").strip()

# number of true negative cases
true_neg_cases = st.text_input("Enter the number of true negative cases: ").strip()

# number of false positive cases
false_pos_cases = st.text_input("Enter the number of false positive cases: ").strip()

# CLEAN AND VALIDATE INPUT
#Run the following code if button is clicked
if st.button("Epidemiology Metric Report Generator"):
    valid_flag = True
    if not city.replace(" ", "").isalpha():
        st.error("Please enter a valid city name with letters.")
        valid_flag = False

    if not disease.replace(" ", "").isalpha():
        st.error("Please enter a valid disease name with letters.")
        valid_flag = False

    if not totpop.isdigit():
        st.error("Invalid input for total population. Enter a positive whole number with no commas.")
        valid_flag = False

    if not reported_cases.isdigit():
        st.error("Invalid input for reported cases. Enter a positive whole number with no commas.")
        valid_flag = False

    if not deaths.isdigit():
        st.error("Invalid input for deaths. Enter a positive whole number with no commas.")
        valid_flag = False

    if not true_pos_cases.isdigit():
        st.error("Invalid input for true positive cases. Enter a positive whole number with no commas.")
        valid_flag = False

    if not false_neg_cases.isdigit():
        st.error("Invalid input for false negative cases. Enter a positive whole number with no commas.")
        valid_flag = False

    if not true_neg_cases.isdigit():
        st.error("Invalid input for true negative cases. Enter a positive whole number with no commas.")
        valid_flag = False

    if not false_pos_cases.isdigit():
        st.error("Invalid input for false positive cases. Enter a positive whole number with no commas.")
        valid_flag = False

    if valid_flag:
        totpop = int(totpop)
        reported_cases = int(reported_cases)
        deaths = int(deaths)
        true_pos_cases = int(true_pos_cases)
        false_neg_cases = int(false_neg_cases)
        true_neg_cases = int(true_neg_cases)
        false_pos_cases = int(false_pos_cases)

    if totpop == 0:
        st.error("Total population cannot be 0.")
        valid_flag = False

    if reported_cases == 0:
        st.error("Reported cases must be greater than 0 for CFR.")
        valid_flag = False


    if valid_flag:
        prevalence = (reported_cases / totpop) * 100
        case_fatality_rate = (deaths / reported_cases) * 100
        mortality_rate = (deaths / totpop) * 100

        sensitivity = (true_pos_cases / (true_pos_cases + false_neg_cases)) * 100
        specificity = (true_neg_cases / (true_neg_cases + false_pos_cases)) * 100
        pos_pre_value = (true_pos_cases / (true_pos_cases + false_pos_cases)) * 100
        neg_pre_value = (true_neg_cases / (true_neg_cases + false_neg_cases)) * 100

    report = (
                "Epidemiology Report:\n"
                "----------------------------------------------\n"
                f"City: {city}\n"
                f"Disease: {disease}\n"
                f"Population: {totpop:,}\n"
                f"Cases: {reported_cases:,}\n"
                f"Deaths: {deaths:,}\n"
                "\n"
                f"Prevalence: {prevalence:.3f}%\n"
                f"Case Fatality Rate: {case_fatality_rate:.3f}%\n"
                f"Mortality Rate: {mortality_rate:.3f}%\n"
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

    st.text(report)
    st.code(report)

