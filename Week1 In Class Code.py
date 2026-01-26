#-------------------------------------------------------
#Week 1 In Class Code
#Name: Najiyah Williamson
#Date: 1/23/26
#-------------------------------------------------------

#----------------------------------
#Built-In Functions, type()
#----------------------------------
type(2)
type(2.5)
x = 2 # variable assignment
type(x)
type(True)
type("Welcome to BIOS 584!")

#----------------------------------
#Variable Assignment with Lists (object)
#----------------------------------
numbers = [2,1,3,4,7]
numbers2 = [11,18,29]
numbers2.append(8)
name = "Trey"

numbers=numbers2
print(numbers)

numbers, numbers2 = [2,1,3,4,7], [11,18,29] #equivalent to...
numbers = [2,1,3,4,7]
numbers2 = [11,18,29]

numbers2=numbers2.append(8) #will get an error-numbers2= {NoneType}None! Don't need variable assignment when working with
## variable objects. Only use object mutation

#----------------------------------
#String methods with strings(imutable object)
#----------------------------------
name = "Najiyah"
name.lower() #expression,returns a new str object
name=name.lower()
print(name)

type(name)
city="new york   "
len(city) #gives length of the object
city.strip() #strips the spaces on the left and right side of the object
print(city.strip) # printing out that a built in method was used on a string object
print(city)
city = city.strip()
city=" new york   ".strip().title()
print(city)