''' Functions and Methods Homework'''
# Complete the following questions:


# Question #1
import string
import math
print('\n*** Question #1 ***')
# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as $$\frac{4}{3} πr^3$$


def sphere_vol(radius):
    return print(f"\tThe volume of a sphere that has radius of {radius} is : {4/3*math.pi*radius**3}")


sphere_vol(2)
sphere_vol(1)
sphere_vol(20)


# Question #2
print('\n*** Question #2 ***')
# Write a function that checks whether a number is in a given range (inclusive of high and low)


def range_check(number, high, low):
    return print(f"\tIs {number}, between {low} and {high}? {low < number < high}")


range_check(3, 1, 10)
range_check(5, 2, 7)


# Question #3
print('\n*** Question #3 ***')
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: .isupper() and .islower()


def up_low_counter(mystring):
    upper_counter = 0
    lower_counter = 0
    other_counter = 0
    for letter in mystring:
        if letter.isupper():
            upper_counter += 1
        elif letter.islower():
            lower_counter += 1
        else:
            other_counter += 1
    return print(f"\tThe No. of upper case characters: {upper_counter}\n\tThe No. of lower case characters: {lower_counter}\n\tThe No. of nonletter characters: {other_counter}")


up_low_counter('Hello Mr. Rogers, how are you this fine Tuesday?')


# Question #4
print('\n*** Question #4 ***')
# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list(initial_list):
    my_unique_list = list(set(initial_list))
    return print(f"\tThe initial list is: {initial_list}\n\tThe unique values list is: {my_unique_list}")


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


# Question #5
print('\n*** Question #5 ***')
# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24


def mutilplyer(num_list):
    final_number = 1
    for x in num_list:
        final_number *= x
    return print(f"\tThe initial list is: {num_list}\n\tThe produce of the list's elements is: {final_number}")


mutilplyer([1, 2, 3, -4])


# Question #6
print('\n*** Question #6 ***')
# Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


def palindrome(my_string):
    my_string = my_string.replace(" ", "")
    my_backwards_string = my_string[::-1]
    if my_backwards_string == my_string:
        return print(f"\tYes '{my_string}' is a palindrome")
    else:
        return print(f"\tNope '{my_string}' is NOT a palindrome")


palindrome('mamaamam')
palindrome('nurses run')
palindrome('nursesrun')


# Question #7
print('\n*** Question #7 ***')
# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
#
# Hint: Look at the string module alphabet=string.ascii_lowercase


def is_pangram(my_string):
    print(f"\tInput string: {my_string}")
    my_strip_string = list(set(list(my_string.replace(" ", "").lower())))
    my_strip_string.sort()
    my_strip_string = "".join(my_strip_string)
    print(f"\tStrip string: {my_strip_string}")
    if my_strip_string == string.ascii_lowercase:
        return print(f"\tYes, we have a panagram\n\t--")
    else:
        return print(f"\tNope, we don't have a panagram\n\t--")


is_pangram("The quick brown fox jumps over the lazy dog")
is_pangram("Crazy Fredrick bought many very exquisite opal jewels")
is_pangram("A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent")


print('\n--- THEND ---')
# Great Job!
