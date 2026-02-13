#-----------------------------
# Week 4 Password generator Code from Lab 1
# Name: Najiyah Williamson
# Date: 2/13/26
#-----------------------------
'''
city = input("Which city did you grow up in?").strip().upper()
animal = input("What is your favorite animal?").strip().lower()
fav_num = int(input("What is your favorite number?"))
special_char = input("Choose a special character from these choices: !@#$%^&*").strip() #Can;t use "select" for some reason
user_password = city[:2] + animal[-2:] + str(fav_num*2) + len(city)*special_char #Use string concatenation
#print(f"{city[:2]}{animal[-2:]}{fav_num*2}{len(city)*special_char}")
print(f"Your generated password is: {user_password}")
'''

#is vs ==
list1 = [1,2,3]
list2 = [1,2,3]
list1 == list2 #True, checks "is the value of list1 and list2 the same?". Checks EQUALITY
list1 is list2 #False, is checks "are these the same object in memory?". Checks IDENTITY


#--------------- Password generator with validation with simple while loops ------------------
#Take in user input for favorite city
city = input("Which city did you grow up in?").strip().upper()
#Validate that user wrote a valid city name. If not valid, make user input city name again
    #while city != city.isalpha(): #NOT VALID CODE
    #while city is not city.isalpha(): #NOT VALID CODE - "is" checks identity, "==" is equality
'''
while city.isalpha() == False: #Technically correct, but not "Pythonic" code
    print("Please enter a valid city name with letters.")
    city = input("Which city did you grow up in?").strip().upper()
'''
while not city.isalpha(): #Best way, pythonic code: reads naturally, shorter and concise
    print("Please enter a valid city name with letters and no spaces.")
    city = input("Which city did you grow up in?").strip().upper()


#Take in user input for favorite animal
animal = input("What is your favorite animal?").strip().lower()
#Validate that input is a string with letters. If not valid, make user input animal name again
while not animal.isalpha():
    print("Please enter a valid animal name with letters and no spaces.")
    animal = input("What is your favorite animal?").strip().lower()


#Take in user input for favorite number
fav_num = input("What is your favorite number?").strip()
#Validate that input is a positive whole number. Can't be floats or words.
'''
while type(fav_num) != int: #will yield infinite while loop. fav_num is ALWAYS a string becuase it's user input
'''
while not fav_num.isdigit():
    print("Invalid input. Enter a positive whole number.")
    fav_num = input("What is your favorite number?").strip()
fav_num = int(fav_num)


#Take in user input for special character
special_char = input("Choose ONE special character from these choices: !@#$%^&*").strip() #Can;t use "select" for some reason
#Validate that input is one of the special characters and is a string
allowed_chars = "!@#$%^&*"
while len(special_char) != 1 or special_char not in allowed_chars:
    print("Please enter a valid special character from these choices: !@#$%^&*")
    special_char = input("Choose ONE special character from these choices: !@#$%^&*").strip()

#Once you verify, that all inputs are valid, generate the user password
user_password = city[:2] + animal[-2:] + str(fav_num*2) + len(city)*special_char
print(user_password)