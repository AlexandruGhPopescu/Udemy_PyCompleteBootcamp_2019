''' Function Practice Exercises - Warmup'''
# Problems are arranged in increasing difficulty:

# Warmup - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve


# WARMUP SECTION:

# LESSER OF TWO EVENS:
print('\n*** F1 LESSER OF TWO EVENS: ***')
#   Write a function that returns the lesser of two given numbers if both numbers are even,
#   but returns the greater if one or both numbers are odd


def less_of_two_evens(a, b):
    print(f"\tThe 2 numbers are {a} and {b}")
    if (a % 2 == 0) and (b % 2 == 0):
        return print(f"\tThey are even and the lesser is: {min(a, b)}\n--- ")
    else:
        return print(f"\tThey are not both even and the greater is: {max(a, b)}\n--- ")


less_of_two_evens(465467, 433543)
less_of_two_evens(46, 45)
less_of_two_evens(622, 530)


# ANIMAL CRACKERS:
print('\n*** F2 ANIMAL CRACKERS: ***')
# Write a function takes a two - word string and returns True if both words begin with same letter


def animal_crackers(my_string):
    check_list = list(my_string.split())
    if (len(check_list) == 2):
        print(f"\tThe 2 words are {check_list[0]} and {check_list[1]}")
        return print(f"\t'They start with the same letter' is a {check_list[0][0] == check_list[1][0]} statement\n--- ")
    else:
        return print("\tPlease input a two-words string... no more, no less. Thank you!\n--- ")


animal_crackers('Rogger Rabbit')
animal_crackers('Forrest Gump')


# MAKES TWENTY:
print('\n*** F3 MAKES TWENTY: ***')
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False


def makes_twenty(a, b):
    print(f"\tThe 2 numbers are: {a} and {b}")
    return print(f"\tIs their sum 20? {(a+b)==20}!\n--- ")


makes_twenty(14.67, 5.26)
makes_twenty(11.22, 8.78)


print('\n--- THEND ---')
