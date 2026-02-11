#-----------------------------------------------------------------------
# Chapter 5 (If Statements) Python Scripts
# Name: Najiyah Williamson
# Date: 2/11/26
#-----------------------------------------------------------------------

# simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
❶     if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for equality
car = 'Audi'
car.lower() == 'audi'

# checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# checking multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

# checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

# checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# examples of Boolean expressions
game_active = True
can_edit = False

#






