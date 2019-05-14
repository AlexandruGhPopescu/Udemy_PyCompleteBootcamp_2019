# ----- IMPORTANT INFO -----
#   We can use break, continue and pass statements in our loops to add additional functionality for various cases
#           - break: Breaks out of the current closest enclosing loop
#           - continue: Goes to the top of the closest elclosing loop
#           - pass: Does nothing at all - like a placeholder for the code you will write later on
#                    -> if you have a loop statement and there is nothing there you will get an error and
#                       the rest of the code will no run

# ------ USING PASS ------
print('\n***')
print("Using 'pass' statement \n")

x = [1, 2, 3]
for item in x:
    pass
print(f"\tThis out was possible thanks to the 'pass' statement")

# ------ USING BREAK ------

print('\n***')
print("Using 'break' statement \n")

name_string = "Samantha"
for letter in name_string:
    if letter == "m":
        break
    print(f"\t{letter}")


# ------ USING CONTINUE ------

print('\n***')
print("Using 'continue' statement \n")

name_string = "Samantha"
for letter in name_string:
    if letter == "a":
        continue
    print(f"\t{letter}")

print('\n--- THEND ---')
