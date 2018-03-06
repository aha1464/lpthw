# This one is like your scripts with argv
# def for define which also inlcude the function name or define the function name
def print_two(*args):
# arg1/2 are the agrument variable for functions *args
# original mistake was made here with arg3 was there is instead of arg2
    arg1, arg2 = args
# the text to printo n screen with the {packages that need to be unpacked}
# the Colon is used to start indentation
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do This
# defined function with a colon
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one arguement
def print_one(arg1):
    print(f"arg1: {arg1}")

    # this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# note function is the same as a mini script
# "run", "call", or "use" a function each means the same thing
