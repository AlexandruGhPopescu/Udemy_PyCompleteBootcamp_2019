""" Statements Assessment Test
    Let's test your knowledge!"""

# Q1:
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
print('\n*** Q1 ***')

st = 'Sam - Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        # to take into account some edventual capital "S"
        # if I make the letter at index 0 in lower case and it's equal to 's'
        print(f"\t{word}")

# Q2:
# Use range() to print all the even numbers from 0 to 10.
print('\n*** Q2 ***')
my_list_q2 = [x for x in range(11) if (x % 2 == 0)]
print(f"\tThe even numbers 'till 11, are: {my_list_q2}")

'''or'''

for x in range(0, 11, 2):
    print(f"\t{x}")

'''or'''
my_list_q2_beta = list(range(0, 11, 2))
print(f"\tThe even numbers 'till 11, are: {my_list_q2_beta}")


# Q3:
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('\n*** Q3 ***')
my_list_q3 = [x for x in range(1, 51) if (x % 3 == 0)]
print(
    f"\tThese are the numbers between 1 and 50 that are divisible by 3:\n\t {my_list_q3}")

# Q4:
# Go through the string below and if the length of a word is even print "even!"
print('\n*** Q4 ***')
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if (len(word) % 2 == 0):
        print(f"\tThe word '{word}' has an even number of letters")

# Q5:
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
print('\n*** Q5 ***')

for x in range(1, 101):
    if (x % 15 == 0):
        print(f"\t{x}: FizzBuzz")
    elif (x % 3 == 0):
        print(f"\t{x}: Fizz")
    elif (x % 5 == 0):
        print(f"\t{x}: Buzz")

# Q6:
# Use List Comprehension to create a list of the first letters of every word in the string below:
print('\n*** Q6 ***')

st = 'Create a list of the first letters of every word in this string'
my_list_q6 = [x[0] for x in st.split()]

print(
    f"\tThese are the first letters of every word in the sentance:\n\t {my_list_q6}")


print('\n--- THEND ---')
# Great Job!
