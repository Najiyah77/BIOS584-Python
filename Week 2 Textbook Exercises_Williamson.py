#-----------------------------------------------------------------------
# Week 2 Lab - Python Textbook Exercises
# Name: Najiyah Williamson
# Due Date: 2/4/26
#-----------------------------------------------------------------------

#------------------------ Exercise 3-4 ----------------------------
friends = ['Keanu', 'Michael', 'SZA']

message1 = f"Hi {friends[0]}, would you like to come over for dinner this Saturday?"
print(message1)

message2 = f"Hi {friends[1]}, would you like to come over for dinner this Saturday?"
print(message2)

message3 = f"Hi {friends[2]}, would you like to come over for dinner this Saturday?"
print(message3)

#------------------------ Exercise 3-6 ----------------------------
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
countries = ['Japan','Morocco','New Zealand', 'Spain', 'China']
print(countries)

print(sorted(countries)) #doesn't change the order permanently but still prints in alphabetical order
print(countries) #the same as the original list

print(sorted(countries, reverse=True)) #doesn't change the order permanently but still prints in reverse alphabetical order
print(countries) #the same as the original list

countries.reverse()
print(countries) #ordered backwards from original list now

countries.reverse()
print(countries) # back to original list order

countries.sort() #alphabetical order
print(countries) #changed the list so that it is in alphabetical order

countries.sort(reverse=True) #reverse-alphabetical order
print(countries) #changed the list so that it is in reverse-alphabetical order

#------------------------ Exercise 3-11 ----------------------------
my_list  = [1,2,3]
#print(my_list[5]) #provides an index error about being out of range

#------------------------ Exercise 4-1 ----------------------------
pizzas = ['White', 'Olive', 'Plain']

#for pizza in pizzas:
    #print(pizza)

for pizza in pizzas:
    print(f"I like {pizza} pizzas!")

print("I really love pizza!")

#------------------------ Exercise 4-11 ----------------------------
pizzas = ['White', 'Olive', 'Plain']

friend_pizzas = pizzas[:]

pizzas.append("Margherita")
friend_pizzas.append("Pineapple")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
