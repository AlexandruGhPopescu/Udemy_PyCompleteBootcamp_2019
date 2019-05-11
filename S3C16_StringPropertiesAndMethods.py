# -------  Strings FAQ -------
# 1. Are strings mutable?
# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)

# 2. How do I create comments in my code?
# You can use the hashtag # to create comments in your code


# Immutabiliy

# string objects do not support item assigment (replacing a specific index)
#   my_string='Sam'
#   my_string[0]= 'P'
# this will throw an error

name = 'Sam'
last_letters = name[-2:]
name = 'P' + last_letters
print(name)

letterz = 'Zzzz'
print(letterz * 10)

x = 'Hello Pandas'
x = x + ' it is beautiful outside!'
print(x)
print(x.upper())
print(x.lower())
print(x.split())

# by default split() splits after the spaces
# but you can give it a parameter to split after a specific character - it does not include that character in the obtained list
print(x.split('i'))
