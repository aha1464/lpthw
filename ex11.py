# What does the end='' do as a function?
print("How old are you?", end='')
# input () means that the user has to input an answer to the printed question
age = input()
print("How tall are you?", end='')
height = input ()
print("How much do you weigh?", end='')
weight = input ()

print(f"So, you're {age} years old, {height} tall and {weight} lbs.")

print("What is your name?", end='')
name = input ()
print("Where do you live?", end='')
live = input ()

print(f"So, your name is {name} and you live in {live}.")
