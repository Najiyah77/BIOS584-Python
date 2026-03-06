#-----------------------------------------------------------------------------------------------------------------------
# Module 6 Functions Exercises:
# This file shows how to define and call functions, and shows the difference between
# functions which use a local scope and functions which use a global scope
# Name:
# Date:
#-----------------------------------------------------------------------------------------------------------------------
#===================================================================
# Functions that only print (but don't return objects)
#===================================================================
#-----------------------------
# Function with no parameters
#-----------------------------
def greet_user(): #how to define a function
    """Display a simple greeting.""" #this is a docstring
    print("Hello!")

greet_user() #Call the function

#-----------------------------
#Function with one parameter
#-----------------------------
def greet_user(username): #username is the parameter (placeholder for info needed to execute the task)
    """ Display a simple greeting."""
    print(f"Hello, {username}!")

greet_user(username = 'jesse') #'jesse','diana' and 'brandon' are arguments (specific info passed to the function)
greet_user(username = 'diana')
greet_user(username = 'brandon')

#-----------------------------
#Function with two parameters
#-----------------------------
def describe_pet(animal, name):
    """Display information about a pet."""
    print(f"\nI have a {animal}.")
    print(f"Its name is {name}.")

#Function calls with positional arguments
describe_pet("hamster", "harry")

# Function calls with keyword arguments
describe_pet(animal = "hamster", name = "harry")
describe_pet(name = "willie", animal = "dog") #order I pass keyword arguments to the function doesn't matter
#----------------------------------------
#Functions with default values
#----------------------------------------
def describe_pet(name, animal="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal}.")
    print(f"It's name is {name}.")

describe_pet(name = "harry", animal = "hamster")
describe_pet("willie") #if willie is a dog, don't need to specify that the animal is a dog since by default
# the function assumes the animal is a dog

#-----------------------------------------------
# Functions where some argument(s) are optional
#-----------------------------------------------
def describe_pet(animal, name=None):
    """Display information about a pet."""
    print(f"\nI have a {animal}.")
    if name: #if name is not None (aka if a name was passed to the function)
        print(f"Its name is {name}.")

describe_pet(animal = "hamster", name = "harry")
describe_pet(animal = "snake") #providing the name is optional for the function to run

#===================================================================
# Functions that return objects after executing a task
#===================================================================
#-----------------------------
# Function that accepts two parameters
# and returns a value
#-----------------------------
def compute_prevalence(pop,cases):
    """ Compute the proportion of a population with a disease."""
    if pop <= 0:
        print("Population shouldn't be 0 or negative, input population again.")
    else:
        prev = cases / pop  # this is a local variable, it is only accessible in the function
        return prev #prev, cases and pop are all local variables (variables that are only accessible within the function)
    #A function is like a trip to Las Vegas. What happens in Vegas, stays in Vegas so you have to return the object
    #otherwise it is not accessible once you leave the function!

#How to call this function
prev_atl = compute_prevalence(pop = 10000,cases = 500)

Pop = 1000 #global variables, variable that is defined and accessible OUTSIDE a function
Cases = 30 #global variable
prev_atl2 = compute_prevalence(pop = Pop,cases = Cases) #It's best not to use the same global and local variables names
print("Prevalence:", prev_atl)

# Functions that use local variables
def calc_tax(amount, tax_rate):
    tax = amount * tax_rate  # tax is a local variable
    return tax               # return statement is necessary

# A function that changes a global variable (not recommended)
tax = 0.0  # tax is a global variable

def calc_tax(amount, tax_rate):
    global tax           # access global variable
    tax = amount * tax_rate  # change global variable

# A local variable that shadows a global variable (not recommended)
tax = 0.0  # tax is a global variable

def calc_tax(amount, tax_rate):
    tax = amount * tax_rate  # tax is a local variable but it has the same name as the global variable
    return tax      # Output: Tax 4.25 (the local variable)

# A function that uses a global constant (okay)
TAX_RATE = 0.05  # TAX_RATE is a global constant
def calc_tax(amount):
    tax = amount * TAX_RATE  # the constant is used here
    return tax

#-----------------------------------------------------------------------------------------------
# Passing mutable objects to a function will change the mutable object
# Example from the Functions Cheat Sheet
#-----------------------------------------------------------------------------------------------
def print_models(unprinted, printed):
    """3d print a set of models."""
    while unprinted: #while unprinted is not an empty list
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)

# Store some unprinted designs,
# and print each of them.
Unprinted = ['phone case', 'pendant', 'ring']
Printed = []
print_models(unprinted = Unprinted, printed = Printed) #function call changes the global variables
print(f"\nUnprinted: {Unprinted}")
print(f"Printed: {Printed}")

#---------------------------------------------------
# Preventing the function from modifying the list
# -> Pass copies (otherwise you are just passing a reference)
#---------------------------------------------------
def print_models(unprinted, printed):
     """3d print a set of models."""
     while unprinted: #while unprinted is not an empty list
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
     printed.append(current_model) #What happens when print.append is outside the while loop?

# Store some unprinted designs, and print each of them.
#for clarity and readability, don't reuse parameter names for the global variable names
original = ['phone case', 'pendant', 'ring']
newlist = []
print_models(unprinted = original[:], printed = newlist[:])
print(f"\nOriginal: {original}")
print(f"Printed: {Printed}")

#Alternative code to make copies: original.copy(), newlist.copy()

#---------------------------------------------------
# Alternative: only use local variables (most memory efficient)
#---------------------------------------------------
def print_models(unprinted, printed):
     """3d print a set of models."""
     while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)
     return printed

#No global variables. I'm directly passing lists into the function
printed_list = print_models(unprinted = ['phone case', 'pendant', 'ring'], printed = [])
print(printed_list)
print(f"\nOriginal: {original}")
print(f"Printed: {Printed}")