# varialbes with its value
people = 20
cats = 30
dogs = 15

# if people (20) are less than cats (30) which there is so it prints the following
# text
if people < cats:
    print("Too many cats! The world is doomed!")

# ask if there are more people that cats which there isnt looking at the variable
# values above so this line will not be printed
if people > cats:
    print("Not many cats! The world is saved!")

# are there less people than dogs, pulling fromthe variable there are not so this
# will not be printed
if people < dogs:
    print("The worls is drolled on!")

# are there more people than dogs? Yes so the text is printed
if people > dogs:
    print("The world is dry!")


# x += 1 is the same as doing x = x + 1 but involves less typing, called increment by operator. Same goes for -=
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

# 1. What do you think the if does to the code under it?
#It looks at the code under it and the values on the variales, then if the
#the statement is true it will print the line, if it is false it won't print the line.
# If this boolean expression is true, then run the code under it; otherwise, skip it.
# 2. Why does the code under the if need to be indented?
#This is so that python knows what block of code a statement belongs to.
# 3. What happens if it isnt indented?
#It will throw up and IndentationError possibly because it does not know where
# this statemen belongs.
# 4. Can you put other boolean expressions from EX27 in this in-statment?
#
# 5. What happens if you change the inital values for people, cats, and dogs?
# different strings are printed depending on which are True and which are False.
