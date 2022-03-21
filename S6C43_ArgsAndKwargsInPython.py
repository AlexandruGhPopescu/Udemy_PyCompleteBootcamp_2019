# ----- IMPORTANT INFO -----
#  *args and **kwargs
#           - *args: arguments
#               -> accepting an abritraty number of arguments
#               -> without predefinig parameters in your function calls
#               -> the values will be passed as elements of a tuple
#               -> so *args takes in no mater how many and creates a tuple
#               -> 'args' can be replaced with anything as long as the '*' stays there
#                           -> *args and *whatever produce the same effect
#               -> 'args' is a term used by convention
#
#           - **kwargs : keywords arguments
#               -> accepting an abritraty number of keyword arguments
#               -> without predefinig parameters in your function calls
#               -> the values will be passed as key:value pairs in a dictionary
#               -> so **kwargs takes in no mater how many pairs
#               -> 'kwargs' can be replaced with anything as long as the '**' stays there
#                           -> **kwargs and **whatever produce the same effect
#               -> 'kwargs' is a term used by convention
#


# ------ FUNCTION CONSTRUCTION *ARGS ------
print('\n***')
print("Function Construction with *args\n")

print('\n--- without *args')


def percentage_parameters(a, b, c=0, d=0, e=0, f=0):
    return print(f"\tThe 5% of {sum((a,b,c,d,e,f))} is: {sum((a,b,c,d,e,f))*0.05}")
# this is the sum o a tuple - sum accepts only 2 parameters


percentage_parameters(7, 995, 144)
# but the maximum of parameters is 5


print('\n--- with *args')


def percentage_parameters_args(*args):
    return print(f"\tThe 5% of {sum(args)} is: {sum(args)*0.05}\n\tThe numbers are: {args}\n\tThe type is: {type(args)}")
# --- SUPER IMPORTANT NOTE ---
# notice args is called without the *


percentage_parameters_args(7, 995, 144, 43, 546, 32, 5)


# ------ FUNCTION CONSTRUCTION *KWARGS ------
print('\n***')
print("Function Construction with **kwargs\n")

print('\n--- with **kwargs')


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"\tMy fruit of choice is {kwargs['fruit']}")
    else:
        print(f"\tI didn't find any fruit here")


myfunc(fruit='apple', veggie='lettuce')
# --- SUPER IMPORTANT NOTE ---
# notice how the key:value pairs are passed as parameters!!!


# ------ FUNCTION CONSTRUCTION *KWARGS ------
print('\n***')
print("Function Construction with both *args and **kwargs\n")

print('\n--- with both *args and **kwargs')


def my_dual_function(*args, **kwargs):
    print(f"\t{args}")
    print(f"\t{kwargs}")
    return print(f"\tHello I would like to buy: \n\t\t {args[0]} {kwargs['food']}\n\t\t {args[2]} {kwargs['animal']}\n\t\t {args[1]} {kwargs['fruit']}")


my_dual_function(10, 12, 4, fruit='oranges', food='eggs', animal='puppies')

print('\n--- TEST CHECK CODE: Functions #9')


def myfunc(*args):
    my_list = list(even_args for even_args in args if (even_args % 2 == 0))
    return print(f"\t{my_list}")


myfunc(12, 3, 5, 8, 7, 98)

print('\n--- TEST CHECK CODE: Functions #10')


def myfunc(my_string):
    alt_string = ''
    for i in range(len(my_string)):
        if (i % 2 != 0):
            alt_string = alt_string + my_string[i].upper()
        else:
            alt_string = alt_string + my_string[i].lower()
    return print(alt_string)


myfunc('The Centaur is a mythical creature')

print('\n--- THEND ---')
