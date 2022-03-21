# ----- IMPORTANT INFO -----
#   Differnet functions to add additional functionality for various cases
#           - RANGE: automaticaly create a sequence of numbers
#           - ENUMERATE: autmaticaly indexing the elements of a string or a list in tuples
#           - ZIP: it zips together two lists and we can recuperate the results as TUPLES
#                   ->the number of tuples will equal to the number of elemets in the shortest list
#           - IN: checks if an element is in a list and returns a boolean
#           - MIN and MAX: getting the minimum or maximum out of a library
#           - SHUFFLE: randomly shuffles arround any sort of list
#                   -> imported from the random library: from random import shuffle
#                   -> it operates in place changing the actual list just like the sort() function
#                       -->assigning it to a variable - my_list_sh = shuffle(my_list) - will return None
#           - RANDINT: generates a random integer in a given range
#                   -> imported from the random library: from random import randint
#                   -> it can be saved in a variable for later use
#                   -> !!! there is another module for cryptographicaly generate random numbers - SECRETS
#           - INPUT: takes input form keyboard as a STRING
#                   -> it can be saved in a variable for later use
#                   -> it can be casted to float or int

from random import shuffle
from random import randint

# ------ USING RANGE ------
print('\n***')
print("Using 'range()' function \n")


# range(end) - the start is by defaut 0
for item in range(4):
    print(f"\t{item}")

print('\n----')

# range(starting, untill)
for item in range(3, 6):
    print(f"\t{item}")

print('\n----')

# range(starting, untill, step)
for item in range(2, 9, 2):
    print(f"\t{item}")

print('\n----')
# casting it to a list

my_CastList = list(range(2, 9, 2))
print(f"\tMy casted range is the following list: {my_CastList}")


# ------ USING ENUMERATE ------
print('\n***')
print("Using 'enumerate()' function \n")


word = "abcdefg"
for item in enumerate(word):
    print(f"\tThis is {item}")

print('\n----')

for index, letter in enumerate(word):
    print(f"\tIndex: {index}")
    print(f"\tValue: {letter}\n")


# ------ USING ZIP ------
print('\n***')
print("Using 'zip()' function \n")


my_list_a = ['a', 'b', 'c', 'd']
my_list_b = [1, 2, 3, 4]
my_list_c = [77, 88, 99, 22, 33, 44, 66]

print(f"\tMy first list: {my_list_a}")
print(f"\tMy second list: {my_list_b}\n")
print(f"\tMy zipped list: {zip(my_list_a, my_list_b)}")
# notice that this just indicated the memory adress where the zip is stored

print('\n----')

my_list_zipped = zip(my_list_a, my_list_b)
print(f"\tMy zipped list in variable: {my_list_zipped}")
# and this as well => you cannot display the zipped list but you can use it

print('\n----')
print(f"\tMy zipped list casted as a list: {list(zip(my_list_a, my_list_b))}")

print('\n----')

for item in zip(my_list_a, my_list_b):
    print(f"\tZipped value: {item}")

print('\n----')

for item in zip(my_list_a, my_list_b, my_list_c):
    print(f"\tZipped value: {item}")

# notice how even though the my_list_c still had elements the touples stopped
# the number of tuples will equal to the number of elemets in the shortest list

# ------ USING IN ------
print('\n***')
print("Using 'in' check function \n")

print(f"\tIs 'a' in my first list: {'a' in my_list_a}")
print(f"\tIs 'a' in my second list: {'a' in my_list_b}")
print(f"\tIs 'a' in the word 'template': {'a' in 'template'}")

print('\n----')

my_dictionary = {'k31': 4, 'k13': 78, 'k11': 432, 'k41': 'toto'}
print(f"\tIs 'k13' a key in my_dictionary : {'k13' in my_dictionary }")
print(f"\tIs 78 a value in my_dictionary : {78 in my_dictionary.values() }")


# ------ USING MIN/MAX ------
print('\n***')
print("Using 'min()' and 'max()' functions \n")

print(f"\tThis is my third list: {my_list_c}")
print(f"\tThis is the min in my third list: {min(my_list_c)}")
print(f"\tThis is the max in my third list: {max(my_list_c)}")


# ------ USING SHUFFLE ------
print('\n***')
print("Using the 'shuffle()' function\n")

print(f"\tThis is my first list: {my_list_a}")
shuffle(my_list_a)
print(f"\tThis is my fisrt list after the first shuffle: {my_list_a}")
shuffle(my_list_a)
print(f"\tThis is my fisrt list after the second shuffle: {my_list_a}")

# ------ USING RANDINT ------
print('\n***')
print("Using 'randint()' function \n")

print(f"\tThis is a random integer between 100 and 2156: {randint(100,2156)}")
print(f"\tAaand another one: {randint(100,2156)}")
my_random_num = randint(100, 2156)
print(f"\tOk, ok, this is the last one: {my_random_num}")


# ------ USING INPUT ------
print('\n***')
print("Using 'input()' function \n")

result_name = input("\tHy! I'm Alex.\n\tWho are you?\n")
print(f"\tHello {result_name}! Nice to meet you.")

result_age = input("\tSo how old are you, {}?\n".format(result_name))
print(f"\t{result_age} is a great age!")
print(f"\tThe type of the age data is {type(result_age)}")

print('\n----')

print("\tOk let's cast that...")
print(f"\tCasted {result_age} to float")
print(f"\tAgain, {float(result_age)} is a great age!")

# it can be casted also into int


print('\n--- THEND ---')
