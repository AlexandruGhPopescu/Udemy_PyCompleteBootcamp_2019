# ----- IMPORTANT INFO -----
# Python deals with the variable names you assign.
# When you create a variable name in Python the name is stored in a name-space.
# Variable names also have a scope, the scope determines the visibility of that variable name to other parts of your code.
#
# This idea of scope in your code is very important to understand in order to properly assign and call variable names.
# In simple terms, the idea of scope can be described by 3 general rules:
#
#         1. Name assignments will create or change local names by default.
#         2. Name references search (at most) four scopes, these are:
#                 -> local
#                 -> enclosing functions
#                 -> global
#                 -> built-in
#         3. Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
#
# LEGB Rule:
#         L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
#         E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
#         G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
#         B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

#  IMPORTANT MENTION
#  One last mention is that you can use the globals() and locals() functions to check what are your current local and global variables.

# ------ L - LOCALS ------
print('\n***')
print("L - Locals\n")

# GLOBAL
name = 'George_Global'


def greet_local():
    # ENCLOSING
    name = 'Sammy_Eclosing'

    def hello():
        # LOCAL
        name = 'John_Local'
        print('\tHello ' + name)

    hello()


greet_local()

# ------ E - ENCLOSING FUNCTION LOCALS ------
print('\n***')
print("E - Enclosing (function locals)\n")

# GLOBAL
name = 'George_Global'


def greet_enclosing():
    # ENCLOSING
    name = 'Sammy_Eclosing'

    def hello():
        # LOCAL
        # name = 'John_Local'
        print('\tHello ' + name)

    hello()


greet_enclosing()

# ------ G - GLOBAL ------
print('\n***')
print("G - Globals\n")

# GLOBAL
name = 'George_Global'


def greet_global():
    # ENCLOSING
    # name = 'Sammy_Eclosing'

    def hello():
        # LOCAL
        # name = 'John_Local'
        print('\tHello ' + name)

    hello()


greet_global()


# ------ G - ALTERING A GLOBAL ------
print('\n***')
print("G - Altering a global variable\n")

x = 50


def func():
    global x
    print('\tThis function is now using the global x!')
    print('\tBecause of global x is: ', x)
    x = 2
    print('\tRan func(), changed global x to', x)


print('\tBefore calling func(), x is: ', x)
func()
print('\tValue of x (outside of func()) is: ', x)


print('\n--- THEND ---')
