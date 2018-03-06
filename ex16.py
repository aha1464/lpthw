# import = the feature argv = argument variables sys = package
from sys import argv
#
script, filename = argv
# printed text that is shown to the user when running the program
print(f"We're going to erase (filename).")
print("If you don't want that, hit CTRL-C (^c).")
print("If you do want that, hit RETURN.")
# input = user input required ("prompt text goes here")
input("?")
# prints ("the text")
print("Opening the file...")
# target = open(user inputed filename in the terminal) 'W' says open this file in 'write mode'
target = open(filename, 'w')
# prints ("the text here")
print("Truncating the file. Goodbye!")
# target command truncate: empties the file.
target.truncate()
# prints("the text" in the terminal)
print("Now I'm going to ask you for three lines.")
# # line1 is the id and input gives the command that the user needs to input info
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: "
# prints ("the text" in the terminal)
print("I'm going to write these to the file.")
# target.write(the text the user inputs in the terminal when prompted)
target.write(line1)
# using ("\n") starts a new line
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# print the ("text")
print("And finally, we close it.")
# targer.close() closes and saves the file that has been created
target.close()
