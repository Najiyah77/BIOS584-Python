#-----------------------------------------------------------------------
# Application 2: Analyzing Asthma Incidents by Air Quality
# Name: Najiyah Williamson
# Due Date: 3/27/26
#-----------------------------------------------------------------------

# The arguments passed into your function are lists called cities_pop , aqi_levels and er_visits .

Cities_pop = [["new York", 8.3], ["Los angeles", 3.8], ["chicago", 2.7], ["Houston", 2.3], ["phoenix", 1.7], ["San Diego", 1.4], ["Dallas", 1.3]]
Aqi_levels = [120, 85, 95, 130, 40, 55, 110]
ER_visits = [20, 10, 8, 25, 5, 12, 18]

def make_aqicity_dict(popcities_list, aqi_list, ervisits_list):
    aqicity_dict = {}

    for (city, pop), aqi, visits in zip(popcities_list, aqi_list, ervisits_list):

        # editing title case
        city = city.title()

        # classifying each city's AQI
        if 0 <= aqi <= 50:
            category = "Good"
        elif 51 <= aqi <= 100:
            category = "Moderate"
        else:
            category = "Unhealthy"

        aqicity_dict[city] = {
            "AQI": aqi,
            "AQI Classification": category,
            "ER visits": visits,
            "Population": pop,
        }

    return aqicity_dict

# calling the function
aqi_dict = make_aqicity_dict(Cities_pop, Aqi_levels, ER_visits)

# sorting by alphabetical order
aqi_dict = dict(sorted(aqi_dict.items()))

print(aqi_dict)

# printing info about New York
print(aqi_dict["New York"]["AQI Classification"])
print(aqi_dict["New York"]["Population"])

# full info about Dallas
print(aqi_dict["Dallas"])
