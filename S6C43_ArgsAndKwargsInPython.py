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
