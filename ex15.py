# import is how you add features to your script from the python feature set.
# argv is the argument variable, a standard name in programming. This variables
# holds the arguments you pass to the python script. Sys = package.
from sys import argv
# The line below unpacks argv so that instead of holding all the arguments, it
# gets assigned the variables you can work with script & filename.
script, filename = argv
# New command open, it takes the paramater and returns the value.
txt = open(filename)
# the text that you want to print out in the terminal. So it prints a little message.
print(f"Here's your file (filename):")
# Here we are calling a function on the txt file called read. What you get back from open is a filename
# which also has commands you can give. You give the file a command by using the . (dot or period).
# text.read() says "Hey txt! Do your read commnd with no parameters!"
print(txt.read())
# print another message to the user here.
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
