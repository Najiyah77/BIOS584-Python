#-----------------------------------------------------------------------
# Week 2 Lab - Python Textbook Exercises
# Name: Najiyah Williamson
# Due Date: 2/4/26
#-----------------------------------------------------------------------

#------------------------ Exercise 3-4 ----------------------------
# Instructions: 3-4. Guest List: If you could invite anyone, living
# or deceased, to dinner, who would you invite? Make a list that includes
# at least three people you’d like to invite to dinner. Then use your
# list to print a message to each person, inviting them to dinner.

friends = ['Keanu', 'Michael', 'SZA']

message1 = f"Hi {friends[0]}, would you like to come over for dinner this Saturday?"
print(message1)

message2 = f"Hi {friends[1]}, would you like to come over for dinner this Saturday?"
print(message2)

message3 = f"Hi {friends[2]}, would you like to come over for dinner this Saturday?"
print(message3)

#------------------------ Exercise 3-6 ----------------------------
# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

friends = ['Keanu', 'Michael', 'SZA']

message4 = f"Hi everyone, I have found a bigger table that accommodates everyone!"
print(message4)

friends.insert(0, 'Kendrick')
friends.insert(2, 'Olivia')
friends.append('Tyler')

    # simple loop
for friend in friends:
    print(f"Hi {friend}, would you like to come over for dinner this Saturday?")

#------------------------ Exercise 3-7 ----------------------------
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

message5 = f"Hi guys, my new dinner table will not arrive in time, so I gotta have max 2 people now."
print(message5)

popped_friends = friends.pop()
print(popped_friends)

message6 = f"Hi {popped_friends}, sorry, but you are no longer invited to my dinner party."
print(message6)

popped_friends = friends.pop()
print(popped_friends)

message7 = f"Hi {popped_friends}, sorry, but you are no longer invited to my dinner party."
print(message7)

popped_friends = friends.pop()
print(popped_friends)

message8 = f"Hi {popped_friends}, sorry, but you are no longer invited to my dinner party."
print(message8)

popped_friends = friends.pop()
print(popped_friends)

message9 = f"Hi {popped_friends}, sorry, but you are no longer invited to my dinner party."
print(message9)

message10 = f"Hi {friends[0]}, you are still invited to my dinner party."
print(message10)

message11 = f"Hi {friends[1]}, you are still invited to my dinner party."
print(message11)

del friends[0]
del friends[0]

print(friends)
#------------------------ Exercise 3-8 ----------------------------
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.




#------------------------ Exercise 3-11 ----------------------------
# 3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.



#------------------------ Exercise 4-1 ----------------------------
# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!



#------------------------ Exercise 4-11 ----------------------------
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.