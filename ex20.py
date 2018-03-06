# import the argument variable module
from sys import argv

# input_file (est.txt) is going to be the argument variable
script, input_file = argv

# first function (mini script): print_all is the function and the f most likely
# stands for file
def print_all(f):
    print(f.read())

# define the funtion as f.seek default (0) read write pointer within the file
def rewind(f):
    f.seek(0)

# readlines() reads until the EOF (end of file) and returns a list containing
# the lines or read 1 line at a time
def print_a_line(line_count, f):
    print(line_count, f.readline())

# tells you the current file is file that has been input into the terminal i.e.
# text.txt, there is no close function?
current_file = open(input_file)

# tell python to print the line in the () with a new line \n
print("First lets print the whole file:\n")

# print all the current file
print_all(current_file)

# tell python to print this text in the terminal
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# define the first line = 1 and 1. first line of text.txt
current_line = 1
print_a_line(current_line, current_file)

# the variable current_line is passed into the function, in that first parameter
# as a recult, 1 is printed
current_line += 1 #current_line = current_line + 1
print_a_line(current_line, current_file)

# now it will print 2 and that new value in the variavle is passed into the
# function
# the function is at the top of the doc, you call it, or use it later and pass
# on values that are used to do what the function does which is print
current_line += 1 # current_line = current_line + 1
print_a_line(current_line, current_file)

# added for good practice
current_file.close()

# Extra Credit
# 1: Write english comments above each line to explain what is going on.
# 2: Each time print_a_line is run you are passing in a variable current_line.
#Write out what current_line is equal to on each function call,
# and trace how it becomes line_count in print_a_line.
# 3: Find each place a function is used, and go check its def to make sure that
# you are giving it the right arguments.
# 4: Research online what the seek function for file does. Try pydoc file and
#see if you can figure it out from there.
# 5: Research the shorthand notation += and rewrite the script to use that.
# += adds another value with the variable's value and assigns the new value to
# the variable.
# Just when I was going to give up...:
# Starting with line 31: current_line += 1 instead of current_line + current_line = 2
