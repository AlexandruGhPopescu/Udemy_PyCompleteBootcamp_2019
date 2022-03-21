# ----- IMPORTANT INFO -----
#  For loops:
#           - many objects in Python are iterable - meaning we can iterate over every element in that object
#               -> example: every element in a list or every character in a string
#           - we can execute for loops to execute a block of code over every iteration
#
#             my_iterable = [1,2,3]
#             for item_name in my_iterable:
#               #do_something for every item


# ------ CONSTRUCTION ------
print('\n***')
print("Construction examples\n")

# ------ EXERCISE 1 ------
print('\n***')
print("Ex1: Print all elements\n")
my_list = [1, 2, 3, 4, 5, 6]
for num in my_list:
    print(f'\t{num}')
# we could have used any variable name instead of 'num', the result would have been the same

# ------ EXERCISE 2 ------
print('\n***')
print("Ex2: Print something for each element\n")
for num in my_list:
    print('\thello')

# ------ EXERCISE 3 ------
print('\n***')
print("Ex3: Print if condition is met\n")

for num in my_list:
    if (num % 2 == 0):
        print(f'\tEven number: {num}')
    else:
        print(f'\tOdd number: {num}')

# ------ EXERCISE 4 ------
print('\n***')
print("Ex4: Sum elements with loop\n")

list_sum = 0
for num in my_list:
    list_sum = list_sum + num
print(f'\tThe sum of my elements is : {list_sum}')

############ STRINGS ############
# ------ EXERCISE 5 ------
print('\n***')
print("Ex5: Loops in strings\n")

my_string = 'TheMarketPlace'
for letter in my_string:
    print(f'\t{letter}')

# IMPORTANT
# in advanced Python coding if we want to do somethin a certain ammout of times
# and we don't need to do something with the actual variable
# we can use _ instead (see example below)

print('\n----')
for _ in "whatever":
    print(f'\tX')

############ TUPLES ############
# ------ EXERCISE 6 ------
print('\n***')
print("Ex6: Loops in tuples\n")

tup = (1, 2, 3)
for item in tup:
    print(f'\t{item}')

print('\n----')

my_tup_list = [(1, 2), (3, 4), (5, 6)]
print(f"\tThe lenght of my list is: {len(my_tup_list)}")


# ------ EXERCISE 7 ------
print('\n***')
print("Ex7: Tuple Unpacking\n")

for item_tup in my_tup_list:
    print(f"\t{item_tup}")

print('\n----')

for (a, b) in my_tup_list:
    print(f"\t{a}")

# IMPORTANT
# works just as well without the () on the a,b in the for
# -> for a, b in my_tup_list:

print('\n----')

for (a, b) in my_tup_list:
    print(f"\t  {b}")

print('\n----')
my_other_tup_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for item in my_other_tup_list:
    print(f"\t{item}")

print('\n----')

for a, b, c in my_other_tup_list:
    print(f"\t{c}")


############ DICTIONARIES ############
# ------ EXERCISE 8 ------
print('\n***')
print("Ex8: Dictionaries Iterations\n")

d = {'k1': 1, 'k2': 2, 'k3': 3}

for element in d:
    print(f"\t{element}")

# IMPORTANT
# notice that by default, when you iterate trough a dictionary you iterate trough its keys
# in order to recuperate the key:value pairs you need to use the items() method
#  <dictionary_name>.items()

print('\n----')

for element in d.items():
    print(f"\t{element}")

print('\n----')

# IMPORTANT
# we can use the same unpacking technique as for tuples

for key, value in d.items():
    print(f"\tThe Key: {key} has the Value: {value} ")

print('\n----')

for dictionary_item in d.values():
    print(f"\tThe Value: {dictionary_item} ")


print('\n--- THEND ---')
