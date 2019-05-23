''' Function Practice Exercises - CHALLENGING PROBLEMS'''
# Problems are arranged in increasing difficulty:

# Warmup - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve


# CHALLENGING PROBLEMS

# SPY GAME:
print('\n*** F1 SPY GAME: ***')
# Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(spy_list):
    print(f"\tThe list of spy numbers: {spy_list}")
    return print(f"\tIs there a 007 in the house? {'007' in ''.join(map(str, spy_list))}\n--- ")


spy_game([1, 2, 4, 0, 0, 7, 5])
spy_game([1, 0, 2, 4, 0, 5, 7])
spy_game([1, 7, 2, 0, 4, 5, 0])


def spy_game_v2(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works

    return len(code) == 1


# COUNT PRIMES:
print('\n*** F2 COUNT PRIMES: ***')
# Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.


# def count_primes(num_max):
#     prime_list = []
#     for n in range(1, num_max + 1):
#         checker = True
#         for m in range(2, int(n**0.5) + 1):
#             if n % m == 0:
#                 checker = False
#         if checker:
#             prime_list.append(n)
#     print(prime_list)


def count_primes(num_max):
    prime_list = []
    for n in range(1, num_max + 1):
        checker = prime_validation(n)
        if checker:
            prime_list.append(n)
    print(
        f"\tThere are {len(prime_list)-1} prime numbers except '1' until {num_max}:\n\t {prime_list}\n--- ")


def prime_validation(num_check):
    checker = True
    for m in range(2, int(num_check**0.5) + 1):
        if num_check % m == 0:
            checker = False
    return checker


count_primes(17)
count_primes(11)
count_primes(16)
count_primes(49)
count_primes(122)
count_primes(100)


def count_primes_v2(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# PRINT BIG:
print('\n*** F3 PRINT BIG: ***')
# Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')
#            out:   *
#                  * *
#                 *****
#                 *   *
#                 *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".


def print_big(letter):
    letter = letter.lower()
    letter_dictionary = {'a': '\t\t  *  \n\t\t * * \n\t\t*****\n\t\t*   *\n\t\t*   *',
                         'b': '\t\t**** \n\t\t*   *\n\t\t*****\n\t\t*   *\n\t\t**** ',
                         'c': '\t\t*****\n\t\t*   *\n\t\t*    \n\t\t*   *\n\t\t*****',
                         'd': '\t\t**** \n\t\t*   *\n\t\t*   *\n\t\t*   *\n\t\t**** ',
                         'e': '\t\t*****\n\t\t*    \n\t\t***  \n\t\t*    \n\t\t*****'}
    return print(f"\t The demanded letter is '{letter}'\n{letter_dictionary[letter]}\n--- ")


def print_big_v2(letter):

    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****',
                5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ', 9: '*    '}

    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5],
                'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5], 'E': [4, 9, 4, 9, 4]}

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

# print_big('a')
# print_big('B')
# print_big('c')
# print_big('d')
# print_big('e')


print('\n--- THEND ---')
