# ----- IMPORTANT INFO -----
#   List Comprehensions
#           - a unique way of creating a list with Python
#           - they are a good alternative to creating lists with for loops and .append() function

# ------ CONSTRUCTION OF A LIST WITHOUT COMPREHENSION METHOD------
print('\n***')
print("Construction of a list without the comprehension method\n")

my_string = 'California'
my_list = []

for letter in my_string:
    my_list.append(letter)
print(f"\tThis is the list: {my_list}")

# this method is used mostly by begginers

print('\n***')
print("Construction of a list with the comprehension method\n")

my_list_comph = [letter for letter in my_string]
print(f"\tThis is the list: {my_list_comph}")

# the first 'letter' is actually the one in the my_list.append(letter) function
# the rest of the function is just de for

print('\n----')

my_list_a = [x for x in 'Madagascar']
print(f"\tThis is the list: {my_list_a}")


print('\n----')
my_list_b = [num for num in range(20, 28)]
print(f"\tThis is the list: {my_list_b}")


print('\n----')
my_list_c = [num**2 for num in range(20, 28)]
print(f"\tThis is the list squared: {my_list_c}")

# is just like we would do my_list_c.append(num**2) function


print('\n----')

my_list_d = [num for num in range(20, 28) if (num**2 % 3 == 0)]
print(f"\tThis is the list for which the square a multiple of 3: {my_list_d}")

print('\n----')

celsius = [0, 10, 20, 34.5]
farenheit = [((9 / 5) * temp + 32) for temp in celsius]

for celsius_temp_num, farenheit_temp_num in zip(celsius, farenheit):
    print(f"\t{celsius_temp_num}°C is {farenheit_temp_num}°Fr")


# the above would be the equivalent of this:
print('\n----')
celsius_bis = [0, 10, 20, 34.5]
farenheit_bis = []
i = 0

for degree in celsius_bis:
    farenheit_bis.append((9 / 5) * degree + 32)
    print(f"\t{degree}°C is {farenheit_bis[i]}°Fr")
    i += 1


# ------ NESTED FORs ------
print('\n***')
print("Construction of a list with nested 'for's\n")

my_list_nest = []

for x in [2, 4, 6]:
    for y in [10, 100, 1000]:
        my_list_nest.append(x * y)
print(f"\tThis is the result of my nested fors: {my_list_nest}")

print('\n***')
print("Construction of a comprehension list with nested 'for's\n")

my_list_nest_comph = [x * y for x in [2, 4, 6] for y in [10, 100, 1000]]
print(
    f"\tNested fors in coprehension list: {my_list_nest_comph}")


print('\n--- THEND ---')
