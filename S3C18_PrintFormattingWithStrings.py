
# ---------- Formatting with the .format() method ----------
print('\n***')
print("Formatting with the .format() method\n")
# print('Some text {} some text {}'.format(value_a, value_b))

print('The format function is soooo {}'.format('cool'))
print('This is a string {} Of course, {}'.format('...or is it?', 'it is ;)'))

print('The {} {} {}'.format('snores', 'dog', 'fat'))
print('The {2} {1} {0}'.format('snores', 'dog', 'fat'))
print('The {2} {1} {0} and {0} all day'.format('snores', 'dog', 'fat'))
print('The {characteristic} {animal} stole my {item}'.format(
    characteristic='sneaky', animal="'coon", item='lemon-pie'))

# ---------- Float formatting follows "{value:width.precision f} ----------"
print('\n***')
print("Float formatting follows \"{value:width.precision f}\"\n")

result = 100 / 777
example_a = 4153.33694444
example_b = 4153.33696444
print(result)
print("The result was {}".format(result))
print("The result was {r}".format(r=result))
print("The result was {r:1.4f}".format(r=result))

# Notice how the rounding is done in the 2 cases
# Also notice that even though the with is at 1, it still prints all the numbers before the decimal

print("The result was {e_a:1.4f}".format(e_a=example_a))
print("The result was {e_b:1.4f}".format(e_b=example_b))

# if we the width is larger than the number before the decimals, it will fill it with spaces

print("The result was {e_b:30.4f}".format(e_b=example_b))


# ---------- Formatting with the f string literral method ----------
print('\n***')
print("Formatting with the f string literral method\n")

# value_a = "bla"
# value_b = 'blu'
# # print(f'Some text {value_a} some text {value_b}')

my_name = 'Papaya Punisher'
age = 3.4
print(f"Hello, I'm {my_name}")
print(f'{my_name} is {age} years old')

print('\n--- THEND ---')
print('Check out https://pyformat.info/ for more info\n')
