# ----- IMPORTANT INFO -----
#  While loops:
#           - many objects in Python are iterable - meaning we can iterate over every element in that object
#               -> example: every element in a list or every character in a string
#           - we can execute while loops to execute a block of code over every iteration as long as a condition is True
#
#             while some_boolean_condition:
#               #do_something
#             else:
#               #do_something_else


# ------ CONSTRUCTION ------
print('\n***')
print("Construction examples\n")


x = 0
while (x < 5):
    print(f"\tThe current value of x is: {x}")
    x += 1  # this is the equivanlent of x = x + 1
else:
    print("\t'x' is not less than 5")

print('\n--- THEND ---')
