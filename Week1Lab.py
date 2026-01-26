#-------------------------------------------------------
#Week 1 Lab - Band Name Generator
#Name: Najiyah Williamson
#Date: 1/23/26
#-------------------------------------------------------
print("Welcome to Najiyah's Band Name Generator")
city = input("Which city did you grow up in?").strip().title()
animal = input("What is your favorite animal?").strip().title()
print(f"Possible band name for you!: {city} {animal}!")
bandname_len = len(city) + len(animal)
print(f"Your band name length is {bandname_len}")

#-------------------------------------------------------
#Experimenting
#-------------------------------------------------------
#Input
#fav_num = int(input("What is your favorite number?"))
#print(fav_num)

