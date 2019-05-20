''' Function Practice Exercises - Level 1'''
# Problems are arranged in increasing difficulty:

# Warmup - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve

# LEVEL 1 PROBLEMS


# OLD MACDONALD:
print('\n*** F1 OLD MACDONALD: ***')
# Write a function that capitalizes the first and fourth letters of a name


def old_macdonald(name):
    cap_name = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return print((f"\tThe name {name} should be written like this: {cap_name}\n--- "))


old_macdonald('maramara')
old_macdonald('septemina')
old_macdonald('macdonald')

# MASTER YODA:
print('\n*** F2 MASTER YODA: ***')
# Given a sentence, return a sentence with the words reversed
#           master_yoda('I am home') --> 'home am I'
#           master_yoda('We are ready') --> 'ready are We'
#   Note: The .join() method may be useful here.
#   The .join() method allows you to join together strings in a list with some connector string.
#   For example, some uses of the .join() method:
#           >>> "--".join(['a','b','c'])
#           >>> 'a--b--c'
#
#   This means if you had a list of words you wanted to turn back into a sentence,
#   you could just join them with a single space string:
#          >>> " ".join(['Hello','world'])
#          >>> "Hello world"


def master_yoda(sentance):
    print(f"\tI say: '{sentance}'")
    yoda_sentance = list(sentance.split())
    yoda_sentance.reverse()
    return print(f"\tYoda mocks me: '{' '.join(yoda_sentance)}'\n--- ")


master_yoda("We need to go Master Yoda")
master_yoda("You need to pet your dog")


# ALMOST THERE:
print('\n*** F3 ALMOST THERE: ***')
# Given an integer n, return True if n is within 10 of either 100 or 200
#       almost_there(90) --> True
#       almost_there(104) --> True
#       almost_there(150) --> False
#       almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number


def almost_there(position):
    print(f"\tWe are at '{position}'. Are we almost there?")
    return print(f"\t{abs(position - 100) < 10 or abs(position - 200) < 10}\n--- ")


almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)

print('\n--- THEND ---')
