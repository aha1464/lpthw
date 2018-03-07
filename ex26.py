# LPTHW EX24

"""print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
print("How much do you weigh?", end=' '
weight = input()"""

# better written as?
age = input("How old are you?\n")
height = input("How tall are you?\n")
weight = input("How much do you weight?\n")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv

script, filename = argv

# filename was spelt wrong
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#print('Let's practice everything.')
#print('You\'d need to know \'bout escapes
      #with \\ that do \n newlines and \t tabs.')

# better written as:
print(f"Let's practice everything.")
print('You\'d need to know \'bout escapes.')
print('\\ that do\n newlines and \t tabs.')


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#print("--------------)
#print(poem)
#print(--------------")

# Better as:
print("--------------")
print(poem)
print("--------------")

# missung a 6 at the end should be five = 10 - 2 + 3 - 6
five = 10 - 2 + 3 - 6
# missing a ) at the end of the string
print(f"This should be five: {five}\n")

# missing : after (started) and missing / in crates = jars 100 formula
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of:{}\n".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.\n")

start_point = start_point / 10

print("We can also do that this way:\n")
# missing an _ in start_point
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.\n".format(*formula))



people = 20
# spelling mistake in cat(e)s
cats = 30
dogs = 15


# missing ("around the string")
if people < cats:
    print ("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

# mising : after dogs
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

# missing : after dogs
if people <= dogs:
    # missing a ) and the end of the string
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
