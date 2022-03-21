#  string[<start_index> : <stop_index> : <step_size>]

my_string = 'Hello Pandas!'
print(my_string[0])
print(my_string[4])
print(my_string[-2])
print(my_string[-1])

my_other_string = 'ABCDEFGHIJK'
print(my_other_string[:3])
print(my_other_string[1:3])

# the <stop_index> sais go up to that position but NOT including

print(my_other_string[::2])

# REMEMBER
# cool reverse string trick

print(my_other_string[::-1])
