# Week 2 Lab - Additional Exercises
# Name: Najiyah Williamson
# Due Date: 2/6/26
#-----------------------------------------------------------------------

#------------------------ Exercise 1 ----------------------------
#STRING MANIPULATION
word = "programming"

print(word[0:5]) #printing the first 5 char, pos indices - EASIER because I didn't need to count the number of characters in "programming."
print(word[-11:-6]) #printing the first 5 char, neg indices

print(word[7:11]) # printing the last 4, pos indices
print(word[-4:]) # printing the last 4, neg indices - EASIER because I don't need to count again

print(word[3:7]) # printing the middle 4 - EASIER since I don't have to go backwards
print(word[-8:-4]) # printing the middle 4

#------------------------ Exercise 2 ----------------------------
#ARITHMETIC OPERATIONS

fav_number = int(input(f"What is your favorite number?"))

math1 = fav_number ** 2 #squared
math2 = fav_number // 3 #divided
math3 = fav_number % 7 #remainder

print(f"Squared: {math1}, Divided: {math2}, Remainder: {math3}")

#------------------------ Exercise 3 ----------------------------
#MODULUS AND SPECIAL CHARACTERS

left = 18 % 30 #getting the remainder after dividing equally

print(left)


#------------------------ Exercise 4 ----------------------------
#PASSWORD LENGTH CHECK

password = input(f"What is your password?")

mathsforpass = 9 - len(password)
new = password + ("!" * mathsforpass) # so if password is shorter, mathsforpass is positive, so ! will be added

print(new)

#------------------------ Exercise 5 ----------------------------
#NUMERICAL LISTS AND FOR LOOPS
#getting odd numbers from 1 to 19

odd_nums = []
for value in range(1, 20, 2):
    odd_nums.append(value)

print(odd_nums)


odd_nums = list(range(1, 20, 2)) #starting at 1, then adds 2 to each value until it reaches 19
