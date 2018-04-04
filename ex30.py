# variable with its value
people = 30
cars = 30
trucks = 30

# if True that cars are greater than people the print.
if cars > people:
    print("We should take the cars.")
# or if True that cars are less than people then print.
elif cars < people:
    print("We should not take the cars.")
# if neither / equal then print.
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
