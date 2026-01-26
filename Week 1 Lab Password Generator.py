#-----------------------------------------------------------------------
# Week 1 Lab - Strong Password Generator
# Name: Najiyah Williamson
# Due Date: 1/30/26
#-----------------------------------------------------------------------
#Hint: you can tweak the bandname generator code that we worked on in class.

print("Welcome to Najiyah's Strong Password Generator")

#Step 1: Ask user for their first name. Strip whitespaces and capitalize the first letter of the user's input
#Create a variable called firstname that points to this info
firstname = input("What is your first name?").strip().title()

#Step 2: print "Hello <insert user's first name here in title case>! Let's create a strong password for you!"
print(f"Hello {firstname}! Let's create a strong password for you!")

#Step 3: Ask the user "Which city did you grow up in?", strip the whitespaces & get uppercase version of the city name.
# Create a variable called city that points to this info
city = input("Which city did you grow up in?").strip().upper()

#Step 4: Ask the user "What is your favorite animal?", strip the whitespaces & get lowercase version of the animal name
# Create a variable called animal that points to this info
animal = input("What is your favorite animal?").strip().lower()

#Step 5: Ask the user "What is your favorite number?". Remember to convert the user input to an integer.
# Create a variable called fav_num that points to this info. Hint: see Section 3.1 in the BIOS 584 Module 1 Notes.
fav_num = input("What is your favorite number?")
fav_num = int(fav_num)

#Step 6: Ask the user "Choose a special character from these choices: !@#$%^&*". Strip whitespace.
#Create a variable called special_char that points to this info.
special_char = input("Choose a special character from these choices: !@#$%^&*").strip()

#Step 7: Generate the user's password using String concatenation (see section 5.3 in Module 1 notes) to combine:
# the first 2 uppercase letters of the user's city they grew up in (see Section 5.5)
s = city
first2 = (s[0:2])

# the last 2 lowercase letters of the user's favorite animal (see Section 5.5)
s1 = animal
last2 = (s1[-2:])

# their favorite number multiplied by 2
s2 = fav_num
times2 = str(fav_num * 2)

# the last portion of the password will be the special character the user chose repeated length of the user's city times.
#     Ex: If the user's hometown city is "Detroit" (which has a length of 7 characters) and they chose "!"
#     as their special character, the last portion of the password is "!!!!!!!" ("!" repeated 7 times). See Section 5.3
special_char2 = str(len(city) * special_char)

# Create a variable called "user_password" that points to this concatenated string
user_password = first2 + last2 + times2 + special_char2

#Step 8. Use an f-string to print out "Your generated password is: insert the user's password here"
#See example input and output in the Canvas assignment
print(f"Your generated password is: {user_password}")