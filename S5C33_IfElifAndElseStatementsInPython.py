# ----- IMPORTANT INFO -----
#  Control Flow (cf):
#           - executing a code after a particular condition has been met
#           - if, elif or else
#           - cf syntax makes use of colons and indetation (whitespace)
#                   -> this intentation is crucial to Python and it sets it appart from other programing languages
#                       if condition:
#                           sequence of code
#                       elif other_condition:
#                           other_sequence of code
#                       ...
#                       elif other_condition:
#                           other_sequence of code
#                       else:
#                           no_condition_met sequence of code


# ------ CONSTRUCTION ------
print('\n***')
print("Construction examples\n")

if True:
    print("\tYep, it's true!")


# ------ EXERCISE 1 ------
print('\n***')
print("Ex1: Food excercice - if\n")

hungry = True
if (hungry):
    print('\tFeed meee!')
else:
    print("\tI'm not hungry")


# ------ EXERCISE 2 ------
print('\n***')
print("Ex2: Location excercice - if/elif/else\n")

location = 'Bank'

if location == 'Auto Shop':
    print("\tCars are soo qiuul!")
elif location == 'Bank':
    print("\tMoney is cool, I guess...")
elif location == 'Store':
    print("\tWelcome to THESToRE!")
else:
    print("\tI don't know much...")


# ------ EXERCISE 2 ------
print('\n***')
print("Ex2: Name excercice - if/elif/else\n")

name = "Jose"

if name == 'Sammy':
    print("\tHello Sammy!")
elif location == 'Brian':
    print("\tHello Brian!")
else:
    print("\tHello! What is your name?")


print('\n--- THEND ---')
