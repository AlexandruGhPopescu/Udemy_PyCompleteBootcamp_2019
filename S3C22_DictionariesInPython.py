# ----- IMPORTANT INFO -----
# Dictionaries
#     - Objects retrieved by key name
#     - Unordered and cannot be sorted
#     - Used to quickly retreive an object without knowing it's location just the (key or the value)
#     - Will insert de value:pair anywhere it deems efficient (no control where it adds the value)
#
# Lists
#     - Objects retieved by location (index)
#     - Ordered sequence and can be indexed, sliced or sorted


# ------ CONSTRUCTION ------
print('\n***')
print("Construction examples\n")

my_dict = {'key1': 'value1', 'key2': 'value2'}
print('\tThe values from my first dictionary are: {}, {}'.format(
    my_dict['key1'], my_dict['key2']))

prices_lookup = {'apple': 2.99, 'oranges': 3.01, 'milk': 5.80}
print(f"\t{prices_lookup['apple']}")

# Note: you can lists and other dictionaries as values in a dictionary

d = {'k1': 'abc', 'k2': [20, 55, 88, 64], 'k3': {
    'insideKey_1': 100, 'insideKey_2': 1304}}
print(f"\t{d['k1']}")
print(f"\t{d['k2'][0]}")
print(f"\t{d['k3']}")
print(f"\t{d['k3']['insideKey_2']}")


# ------ ALTERING VALUES ------
print('\n***')
print("Altering Values\n")

print(f"\tBefore: {d}")
d['k1'] = d['k1'].upper()
d['k2'].sort()
d['k3']['insideKey_2'] = 'XXXX'
# remember that sort function does the sorting 'on the fly' so no need for reasignement
print(f"\tAfter: {d}")


# ------ ADDING NEW VALUES ------
print('\n***')
print("Adding New Values\n")

my_dict_beta = {'k1': 100, 'k2': 200, 'k3': 300}
print(f"\t My initial dictionay: {my_dict_beta}")
my_dict_beta['kx'] = 456
print(f"\t My final dictionay: {my_dict_beta}")

# ------ RETURNIG KEYS/VALUES ------
print('\n***')
print("Returning Keys/Values\n")

print(f"\tThe values are: {d.values()}")
print(f"\tThe keys are: {d.keys()}")
print(f"\tThe items are: {d.items()}")

# Dictionaries FAQ
# 1. Do dictionaries keep an order? How do I print the values of the dictionary in order?
# Dictionaries are mappings and do not retain order!
# If you do want the capabilities of a dictionary but you would like ordering as well,
# check out the ordereddict object lecture later on in the course!

print('\n--- THEND ---')
