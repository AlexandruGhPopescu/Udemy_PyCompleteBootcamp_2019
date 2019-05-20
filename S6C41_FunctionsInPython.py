# ----- IMPORTANT INFO -----
#  Functions
#           - allow us to create blocks of code that can be easily exectuted many times,
#               -> without needing to constantly rewrite the the entire block of code
#           - return :
#               -> keyword used at the end of the funciton as a result of its execution
#               -> also allows to assign the output of the function to a new variable
#           - DOCSTRING:
#               -> usefull information about the function
#               -> visible with the help(name_of_function) method
#           - function construction template:
#                       def name_of_function(<paramater>) :
#                           """
#                           DOCSTRING: Infromation about the function
#                           """
#                           block of code
#                       return the_block_of_code_result


# ------ FUNCTION CONSTRUCTION ------
print('\n***')
print("Function Construction\n")


print('\n--- ')


def name_function():
    """
    DOCSTRING: Function_1 - Made for DOCSTRING check with help()
    INPUT: No input
    OUTPUT: 'Hello'
    """
    print("Hello")


help(name_function)


print('\n--- ')


def say_hello(name="NAME"):
    # we added a default value to name the
    # 'NAME' will be used if no other value is given when the funtion is called: say_hello()
    # this is done to avoid errors
    """
    DOCSTRING: Function_2 - Argument
    INPUT: name
    OUTPUT: 'Hello <name>'
    """
    return (f"\t The result of f2 is: Hello {name}")


f2_result = say_hello('Jose')
print(f2_result)


print('\n--- ')


def addition_function(num1, num2):
    return num1 + num2


f3_result = addition_function(4.5, 44)
print(f"\tThe result of f3 is: {f3_result}")

# ------ SOLVING PROBLEMS WITH FUNCTIONS ------
print('\n***')
print("Solving problems with functions\n")

print('\n*** P1 ***')
# Find out if the word 'dog' is in a string


def check_string(my_string):
    check_variable = list(my_string.lower().split())
    if check_variable.__contains__('dog'):
        return True
    else:
        return False


p1_result = check_string("My Dog is awesome!")
print(f"\tThe result of p1 is: {p1_result}")


def check_string_course(a_string):
    return 'dog' in a_string.lower()


print(check_string_course("I dogged this one..."))


print('\n*** P2 ***')
# PIG LATIN
#   if word starts with a vowelm add 'ay' to end
#   if word does not start with a vowel, put first letter at the end and then add 'ay'
#   'word' --> 'ordway'
#   'apple' --> 'appleay'


def pig_latin(my_word):
    if my_word[0] in 'aeiou':
        pigl_word = my_word + 'ay'
        return print(f"\tThe word bar {my_word} in pig latin is: {pigl_word}")
    else:
        pigl_word = my_word[1:] + my_word[0] + 'ay'
        return print(f"\tThe word bar {my_word} in pig latin is: {pigl_word}")


pig_latin('bar')
pig_latin('alter')


print('\n--- THEND ---')
