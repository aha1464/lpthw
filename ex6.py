# the number of peopl are listed below.
types_of_people = 10
# x = the text that is written here.
x = f"there are {types_of_people} types of people."
# listing of the code and the human language.
binary = "binary"
do_not = "don't"
# the value of y in the code to pull in the info as well as the embedded variable.
y = f"Those who know {binary} and those who {do_not}."
# the 2 opening lines x & y as the opening statement when running the programme.
print(x)
print(y)
# the next 2 statement with the variables of x & y embeded with other info.
# the 2 below are also strings within a string.
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
