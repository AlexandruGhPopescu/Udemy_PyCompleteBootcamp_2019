
"""Objects and Data Structures Assessment Test
Test your knowledge.
Answer the following questions"""

'''######### PART 1 - Object Types and Data Structures #########'''

# Q1:
#     Write a brief description of all the following Object Types and Data Structures we've learned about:
#
#     Numbers:
#           - int (Mathematical integers), float(decimal numbers)
#     Strings:
#           - ordered sequence of random caracters (letters, numbers, special caracters)
#           - indexed, mutable
#     Lists:
#           - ordered sequence of random objects and data structures (strings, int, floats, other lists)
#           - indexed, mutable
#     Tuples:
#           - odered sequence of random objects and data structures (strings, int, floats, other lists)
#           - indexed, immutable
#     Dictionaries:
#           - unordered sequnece of key:value pairs of random objects and data structures (strings, int, floats, other lists, dictionaries)
#           - not indexed, no user control of where - at which position - the pairs are kept
#

'''######### PART 2 - Numbers #########'''

# Q2:
#     Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#     Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
#
#               calculus = ((4 + 6) ** 2 * (3.4 + 6.6) + 7.5) / 10 - 0.5
#               print(calculus)
# Q3:
#     Answer these 3 questions without typing code. Then type code to check your answer.
#
#     What is the value of the expression 4 * (6 + 5) = 44
#     What is the value of the expression 4 * 6 + 5 = 29
#     What is the value of the expression 4 + 6 * 5 = 34
#
#
# Q4:
#     What is the type of the result of the expression 3 + 1.5 + 4?
#                   float or FloatingPointNumber
#
# Q5:
#     What would you use to find a number’s square root, as well as its square?
#     # Square root:  math.sqrt(x) or x**0.5
#     # Square: x**2

'''######### PART 3 - Strings #########'''
# Q6:
#     Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
#         s = 'hello'
#         # Print out 'e' using indexing: print(s[1])
# Q7:
#     Reverse the string 'hello' using slicing:
#         s = 'hello'
#         # Reverse the string using slicing: s = s[::-1]
# Q8:
#     Given the string hello, give two methods of producing the letter 'o' using indexing.
#     s = 'hello'
#     # Print out the 'o'
#     # Method 1: print (s[-1])
#     # Method 2: print (s[4])

'''######### PART 4 - Lists #########'''
# Q9:
#     Build this list[0, 0, 0] two separate ways.
#     # Method 1: list = [0, 0, 0]
#     # Method 2: list = [0]*3
# Q10:
#     Reassign 'hello' in this nested list to say 'goodbye' instead:
#         list3 = [1, 2, [3, 4, 'hello']]
#         list3[2][2] = 'goodbye'
# Q11:
#     Sort the list below:
#       list4 = [5, 3, 4, 6, 1]
#       list4.sort()
#       print(list4)


'''######### PART 5 - Disctionaries #########'''
# Q12:
#     Using keys and indexing, grab the 'hello' from the following dictionaries:
#
#         d = {'simple_key': 'hello'}
#         # Grab 'hello' : d['simple_key']
#
#         d = {'k1': {'k2': 'hello'}}
#         # Grab 'hello':  d['k1']['k2']
#
#         # Getting a little tricker
#         d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
#         # Grab hello :  d['k1'][0]['nest_key'][1][0]
#
#         This will be hard and annoying!
#         d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
#         # Grab hello : d['k1'][2]['k2'][1]['tough'][2][0]

# Q13:
#     Can you sort a dictionary? Why or why not?
#           it is unordered - not based on indexes + sort function not availabe
#       Course_Answer: No! Because normal dictionaries are mappings not sequences

'''######### PART 6 - Tuples #########'''
# Q14:
#     What is the major difference between tuples and lists?
#           Mutability/immutability - Lists/tuples
# Q15:
#     How do you create a tuple?
#           same way you create a list but you just use () insead of []


'''######### PART 7 - Sets #########'''
# Q16:
#     What is unique about a set?
#           the fact that all the values inside the set are unique
# Q17:
#     Use a set to find the unique values of the list below:
#         list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
#         print(set(list5))

'''######### PART 8 - Booleans #########'''

# For the following quiz questions, we will get a preview of comparison operators. In the table below, a = 3 and b = 4.
# Operator | Description Example
#     ==   |  If the values of two operands are equal, then the condition becomes true. (a == b) is not true.
#     !=   |  If values of two operands are not equal, then condition becomes true. (a != b) is true.
#     >    | If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
#     <    | If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
#     >=   |  If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. (a >= b) is not true.
#     <=   |  If the value of left operand is less than or equal to the value of right operand, then condition becomes true. (a <= b) is true.
#
# Q18:
#     What will be the resulting Boolean of the following pieces of code(answer fist then check by typing it in!)
#     2 > 3         - False
#     3 <= 2        - False
#     3 == 2.0      - False
#     3.0 == 3      - True
#     4**0.5 != 2   - False
# Q19:
#     Final Question: What is the boolean output of the cell block below?
#     l_one = [1, 2, [3, 4]]
#     l_two = [1, 2, {'k1': 4}]
#     l_one[2][0] >= l_two[2]['k1'] - False


########### Great Job on your first assessment! ###########
