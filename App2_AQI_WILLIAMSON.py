#-----------------------------------------------------------------------
# Application 2: Analyzing Asthma Incidents by Air Quality
# Name: Najiyah Williamson
# Due Date: 3/27/26
#-----------------------------------------------------------------------
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Diego", "Dallas"]
aqi_levels = [120, 85, 95, 130, 40, 55, 110]
er_visits = [20, 10, 8, 25, 5, 12, 18]
high_population_cities = ["New York", "Los Angeles", "Chicago", "Houston"]

# using zip() loop to list comprehension
mod_info = list(zip(cities, aqi_levels, er_visits))

# title heading
print("\n""City-wise AQI Classification: ")

# using boolean and if else statements
categories = []
for city, aqi, visits in mod_info:
    if 0 <= aqi <= 50:
        category = "Good"
    elif 51 <= aqi <= 100:
        category = "Moderate"
    else:
        category = "Unhealthy"

    categories.append(category)
    print(f"{city}: {aqi} ({category})")


# title heading
print("\n""Cities with either Unhealthy AQI or ER visits > 15: ")

# identifying cities where either the AQI is unhealthy or the numbre of asthma-realted ER visits exceeds 15
for city, aqi, visits in mod_info:
    if aqi >= 101 or visits > 15:
        print(f"{city} (AQI: {aqi}, ER Visits: {visits})")

# title heading
print("\n""High-population cities with AQI > 100: ")

# cities that are in high_population_cities list and have AQI above 100
for city, aqi in zip(cities, aqi_levels):
    if city in high_population_cities and aqi > 100:
        print(f"{city} (AQI: {aqi})")

# title heading
print("\n""Other cities with AQI > 100: ")

# other  cities with high AQI
for city, aqi in zip(cities, aqi_levels):
    if city not in high_population_cities and aqi > 100:
        print(f"{city} (AQI: {aqi})")

# counting how many cities are NOT classified as having "Good" AQI
not_good_count = sum(cat not in ["Good"] for cat in categories)
print("\nNumber of recorded cities that do not have 'Good' AQI:", not_good_count)

# the city with the highest AQI
max_aqi = max(aqi_levels)
index_max = aqi_levels.index(max_aqi)
city_max = cities[index_max]

print(f"\nCity with the highest Air Pollution: {city_max} (AQI: {max_aqi})")