my_int_list = [1, 2, 3]
my_mixt_list = ['Just a string', 100, 8.754]
my_string_list_a = ['One', 'Two', 'Three']
my_string_list_b = ['Four', 'Five', 'Six', 'Seven', 'Eight']

print(my_int_list)
print(my_mixt_list)
print(my_string_list_a)
print(my_string_list_b)


# indexing
print('\n***')
print("Indexing\n")

print(my_string_list_a[0])

# slicing
print('\n***')
print("Slicing\n")

print(my_string_list_a[:1])
print(my_string_list_b[1:3])

# concatenation
print('\n***')
print("Concatenation\n")

my_string_list_c = my_string_list_a + my_string_list_b
print(my_string_list_c)

# mutability
print('\n***')
print("Mutability\n")

# oposed to strings, in list you can alter the elements at different indexes
my_string_list_d = my_string_list_c
print(my_string_list_d)
my_string_list_d[0] = 1
print(my_string_list_d)

# appending
print('\n***')
print("Appending\n")

# adding an element at the end of a list

my_string_list_d.append('Nine')
print(my_string_list_d)

# popping
print('\n***')
print("Popping\n")
# remove an element at the end of a list

print('\tString_list_D before popping: \n\t{}\n'.format(my_string_list_d))
popped_elements = [my_string_list_d.pop()]
print('\tPopped element: \n\t{}\n'.format(popped_elements))
print('\tString_list_D after popping without argument: \n\t{}\n'.format(my_string_list_d))

popped_elements.append(my_string_list_d.pop(3))
print('\tPopped element: \n\t{}\n'.format(popped_elements))
print('\tString_list_D after popping with argument: \n\t{}\n'.format(my_string_list_d))

# sorting
print('\n***')
print("Sorting\n")

alphabeth_list = ['q', 'e', 't', 'a', 'r', 'x', 'j', 'b']
fibonacci_list = [3, 21, 8, 1, 5, 2, 13, 1]

print('\tMixedUp letters: \n\t{}\n'.format(alphabeth_list))
print("\tMixedUp Fibonacci's set: \n\t{}\n".format(fibonacci_list))

alphabeth_list.sort()
fibonacci_list.sort()

print('\tOrdered alphabeticaly: \n\t{}\n'.format(alphabeth_list))
print("\tCorrect Fibonacci's set: \n\t{}\n".format(fibonacci_list))

# REMARK
# the sorting is done in place so doing something like
#       my_new_list = my_list.sort()
# will return the None Value
#
# the way to place the sorted list in a new list is:
#       my_list.sort()
#       my_new_list = my_list


# reversing
print('\n***')
print("Reversing\n")

print("\tCorrect Fibonacci's set: \n\t{}\n".format(fibonacci_list))
fibonacci_list.reverse()
print("\tReversed Fibonacci's set: \n\t{}\n".format(fibonacci_list))

# Lists FAQ
# 1. How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?
# You would just add another set of brackets for indexing the nested list, for example: my_list[2][1] .
# We'll discover later on more nested objects and you will be quizzed on them later!


print('\n--- THEND ---')
