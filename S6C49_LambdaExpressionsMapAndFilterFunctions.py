# ----- IMPORTANT INFO -----
#  Lambda expressions
#       A quick way to create anonimous functions
#       They are also known as one time functions - you don't even name because you only use the once
#
#  Map function
#        A buit in function of Python
#        Takes in a already defined function and a parameter to which it applies that function
#           -> see the example with the square function below
#               --> map(<previously_created_function>, <element_the_function_applies_to>)
# Filter function
#        A buit in function of Python
#        Takes in a already defined function
#           -> this function only performs a check and returns a Boolean
#        And a parameter, list that it verifies using that boolean-retun function
#        It returns only the values that fit the conditions described in the above mentioned function
#           -> see the example below
#               --> map(<previously_created_function_that_retuns_a_boolean>, <element_the_function_verifies>)

# ------ MAP FUNCTION CONSTRUCTION ------
print('\n***')
print("Construction of Map() examples\n")


def square_num(num):
    return num**2


def square_list(initial_list):
    # notice that the square_num function is called without the parantheses in map()
    sq_list = list(map(square_num, initial_list))
    return print(f"\tThe initial list is: {initial_list}\n\tThe squared list using the square_num function is: {sq_list}")


square_list([2, 3, 4, 5, 6, 11])

print('\n--- ')


def splicer(word):
    if len(word) % 2 == 0:
        return print(f"\tThe character number in '{word}' is: EVEN")
    else:
        return print(f"\tThe character number in '{word}' is: ODD")


def splicer_list(my_strings_list):
    words_list = my_strings_list.split()
    # notice that the splicer function is called without the parantheses in map()
    list(map(splicer, words_list))
    return print(f"\t{words_list}")


print('\n--- ')

splicer_list('The apple is still green and stuck on the branch')


# ------ MAP FUNCTION CONSTRUCTION ------
print('\n***')
print("Construction of Filter() examples\n")


def check_even(num):
    return (num % 2 == 0)


def number_analiser(my_numbers):
    print(f"\tInitial numbers list: {my_numbers}")
    print(
        f"\tList after sorting for even with filter(): {list(filter(check_even, my_numbers))}")


number_analiser([1, 2, 3, 4, 5, 6, 7])


# ------ MAP FUNCTION CONSTRUCTION ------
print('\n***')
print("Construction of map() and filter() with 'lambda' expresions examples\n")

print('\n*** map() with lambda')

# Remider - the inital non-lambda expresion
# def square_num(num):
#     return num**2

# lambda <function argument> : <function_return>


def square_list_lambda(initial_list):
    sq_list = list(map(lambda num: num**2, initial_list))
    # sq_list = list(map(square_num, initial_list)) - the inital non-lambda expresion
    return print(f"\tThe initial list is: {initial_list}\n\tThe squared list using the lambda function is: {sq_list}")


square_list_lambda([2, 3, 4, 5, 6, 11])

print('\n--- ')

print('\n*** filter() with lambda')


def number_analiser_lambda(my_numbers):
    print(f"\tInitial numbers list: {my_numbers}")
    print(
        f"\tList after sorting for even with filter() and lambda: {list(filter(lambda num: num % 2 == 0, my_numbers))}")


number_analiser_lambda([1, 2, 3, 4, 5, 6, 7])


print('\n--- ')


def get_letter(names_list):
    print(
        f"\t{names_list} \n\t The names that have the third letter 'a' are: {list(filter(lambda name: name[2] == 'a', names_list))}")


get_letter(['Alex', 'John', 'Liana', 'Cassandra', 'Evageline'])

print('\n--- THEND ---')
