# ----- IMPORTANT INFO -----
# Tuples
#     - Like lists only diffences
#           -> they are immutable
#           -> use parantheses to define them my_tuple = (value1, value2 ,...)
#    - mainly used in more advanced coding when you want to make sure that values don't get changed, flipped or reasigned


# ------ CONSTRUCTION ------
print('\n***')
print("Construction examples\n")

my_tuple = (12, 23, 34)
my_list = [45, 56, 67]

print(f"\t This is a {type(my_tuple)} : {my_tuple}")
print(f"\t This is a {type(my_list)} : {my_list}")


# ------ FUNCTIONS (count, index) ------
print('\n***')
print("Functions (count(), index())\n")

my_tup = ('a', 'a', 'b', 'x', 'a', 'r', 'd', 'a', 'y', 'x', 'a', 'c', 'd')
print(f"\t Element 'a' appears {my_tup.count('a')} times in my_tup")
print(
    f"\t Element 'd' appears for the very first time at possition {my_tup.index('d')} in my_tup")


print('\n--- THEND ---')
