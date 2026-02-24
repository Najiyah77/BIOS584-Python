#-----------------------------------------------------------------------
# Application 3: Flagging High Air Pollution Cities with Loops
# Name: Najiyah Williamson
# Due Date: 2/27/26
#-----------------------------------------------------------------------

# original code
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
pollution_levels = [45, 78, 33, 60, 40]
threshold = 50

high_pollution_cities = [] # Stores high pollution cities

for i in range(len(cities)) : # Iterates through each city
    if pollution_levels[i] > threshold : # Checks for high pollution
        high_pollution_cities.append(cities[i]) # Collect city name

print(high_pollution_cities) # print list of high pollution cities

#-----------------------------------------------------------------------
# rewriting the program...
#-----------------------------------------------------------------------

# using enumerate() function
en_high_pollution_cities = []
for i, pollution in enumerate(pollution_levels):
    if pollution > threshold:
        en_high_pollution_cities.append(cities[i])

print(en_high_pollution_cities)

# using zip() function
zip_high_pollution_cities = []
for pollution, city in zip(pollution_levels, cities):
    if pollution > threshold:
        zip_high_pollution_cities.append(city)

print(zip_high_pollution_cities)

# list comprehension
lc_high_pollution_cities = [cities[i] for i in range(len(cities)) if pollution_levels[i] > threshold]
print(lc_high_pollution_cities)