from sys import argv
# Read the WYSS section for how to run this
script, first, second, third, fourth = argv
# when you run the script you put the variable in the terminal to be displayed

print(">>> argv=", repr(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is", third)
print("your fourth variable is", fourth)
# input variable and tag, with prompt question that the user needs to answer
name = input("What is your name?")
day = input("What day it is?")
year = input("What year is it?")
# difference between argv and input is where the user is required to give input
# agrv means input it required on running the script on the command line
# input means that an input is required using the keyboard while the script is running
print(f"So your name is {name} and today is {day}, {year}.")
