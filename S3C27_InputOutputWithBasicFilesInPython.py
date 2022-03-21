# ----- IMPORTANT INFO -----
# For this lecture we will use the following auxiliary documents
#     - S3C27_ZAUX_MyFile.txt
#

# ------ WORKING WITH A FILE ------
print('\n***')
print("Working with a file\n")


print('\n**')
print("Opening file - the 'heavy' way\n")

# in order to work with a file we use a variable and the open method
# we open the file and place the content in the varaible

my_file = open('S3C27_ZAUX_MyFile.txt')
# to open a file that is outside the script directory we use the path of the file
#       - for Windows open("C:\\Users\\UserName\\Folder\\test.txt")
#               -> the first '\' is to escape the second one
#               -> otherwise in the example above, it would have taken \test.txt has <tab>est.txt
#       - for Unix and MacOS open("/Users/UserName/Folder/test.txt")

print('\n**')
print("Read a file as one line\n")

print(f"\tThe '.read()' function 1st output: {my_file.read()}")

# IMPORTANT
# the .read() function uses a cursor, so after the first read it reaches the end
# that for every next read the counter should be set to zero using .seek(0)
print(f"\tThe '.read()' function 2nd output: {my_file.read()}")
my_file.seek(0)
print(f"\tThe '.read()' function 2nd output after seek(0): {my_file.read()}")


print('\n**')
print("Read a file as a list of lines\n")

my_file.seek(0)
#  notice I've reset the cursor
print(f"\tThe '.readlines()' function 1st output: {my_file.readlines()}")


print('\n**')
print("Closing a file\n")

# IMPORTANT
# closing a file after having it open with the 'open()' function  is crucial !
# otherwise the file will remain in the system as used by Pyhton
# therefore you will not be able to use it with other programs, in Python scripts or delete it
# this can also be the cause of a lot of errors, so:

my_file.close()

print('\n**')
print("Opening file the 'proper' way - 'with open(<file_path>) as <variable> : '\n")

with open('S3C27_ZAUX_MyFile.txt') as my_file_beta:
    content = my_file_beta.read()
    print(f"\tThis is the content of my_file_beta {content}")

# IMPORTANT
# now I no longer have to close the file or worry about that
# notice the intentation (it was done automaticaly) - like the one form a method
# the code I use for that file shloud be wrote under the 'with open...'
# dont forget the ':' at the end of 'with open(<file_path>) as <variable> : '


print('\n**')
print("File permissions - mode='r'/'w'\n")

# IMPORTANT
# the mode parameter in the open() function tells what the lines of code can do with the file
#           -> 'r' - read only (read it)
#           -> 'w' - write only (overwrites existing files or creates new ones)
#           -> 'a' - append only (adding more lines to end of a file such as a .txt)
#           -> 'r+' - read and write
#           -> 'w+' - write and reads (overwrites existing files or creates new ones)


with open('S3C27_ZAUX_MyFile.txt', mode='r') as my_file_beta:
    content = my_file_beta.read()
    print(f"\tThis is the content of my_file_beta {content}")

# if you specify the write mode and you try read the file like below, you will get an error
#   with open('S3C27_ZAUX_MyFile.txt', mode='w') as my_file_beta:
#       content = my_file_beta.read()
#       print(f"\tThis is the content of my_file_beta {content}")

print('\n**')
print("Creating/Writing to a file\n")


with open('S3C27_ZAUX_MyCreatedFile.txt', mode='w+') as my_file_tau:
    my_file_tau.write("This is a file that I've just created using mode='w+'")
    content_tau = my_file_tau.read()
    print(f"\tThis is the content of fresh my_file_tau {content_tau}")


print('\n--- THEND ---')
