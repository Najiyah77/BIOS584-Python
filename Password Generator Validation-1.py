#-----------------------------
#Password generator Code from Lab 1
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