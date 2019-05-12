# ----- IMPORTANT INFO -----
# Sets
#     - UNORDERED collections of unique elements
#           -> ONE representative of the same object


# ------ CONSTRUCTION ------
print('\n***')
print("Construction examples\n")

my_set = set()
print(f"\t This is a {type(my_set)} : {my_set}")

# ------ OPERATIONS ------
print('\n***')
print("Operations examples\n")

my_set.add(1)
my_set.add(2)
print(f"\t The set after adding elements: {my_set}")

my_set.add(2)
print(f"\t The set after adding the same element twice: {my_set}")

# ------ CASTING LISTS TO SETS ------
print('\n***')
print("Casting lists to sets\n")

my_list = ['a', 'a', 'b', 'x', 'a', 'r', 'd', 'a', 'y', 'x', 'a', 'c', 'd']
print(f"\t This is the initial list {my_list}")
print(f"\t This is the list casted into a set {set(my_list)}")
print(f"\t This is a string casted directed into a set {set('Mississippi')}")

# the display is like that of a dictionay {} but without the key:value pairs
# set('Mississippi') - works like a charm even though it's a string

print('\n--- THEND ---')
