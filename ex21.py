# LPTHW EX21

# defining the function of add with 2 arguments. I add a and b then return them
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# defining the function of subtract
def subtract(a, b):
    print(f"SUBTRACKTING {a} - {b}")
    return a - b

# defining the function of multiply
def multiply(a, b):
    print(f"MULTIPLING {a} * {b}")
    return a * b

# defining the function of divide
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# print the text in the string and add a new line
print(f"let's do some math with just functions!\n")

# defining age, height, weight & iq by addition, subraction, multiplying and
# dividing with the (the values, required)
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# print the text with their {variable}
print(f"Age: {age}, Height {height}, Weight {weight}, IQ {iq}\n")

# a puzzle for the extra credit, type it in anyway

# print the text below in the terminal
print(f"Here is the puzzle.")

# WTF, I have no idea??? Inside out: (iq, 2)(/ weight)(multiply by height)
#(subtract age) add
# 50/2 = 25
# 180 * 24 = 4500
# 74 - 4500
# 35 + -4426 = -4391
#
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print("24 + 34 / 100 - 1023")

# Extra Credit:
# 1. If you aren't really sure what return does, try writing a few of your own
# functions and have them return some values. You can return anything that you
# can put to the reight of an =
# 2. At the end of hte script is a puzzle. I'm taking th return value of one
# function and using it as the argument of an other funtion. I'm doing this in
# a chain so that I'm kind of creating a formula using the function. It looks
# really weird, but if you run the sript, you can see the results.
# 3. Once you have the formula worked out for the puzzle, get in there and see
# what happens when you modify the parts of the functions. Try to change it on
# purpose to make another value.
# 4. Do the inverse. Write a simsple forumula and use the functions in the
# same way to calculate it.
