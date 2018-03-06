# LPTHW EX19

# comment out 1 line
""" comment out multiple lines"""
""" Variables in the function are not connected to the variables in the script
defined variables below """

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(">>> cheese_count=", cheese_count, "boxes_of_crackers=", boxes_of_crackers)
    print(f"You have {cheese_count} packets of cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.")
    print("<<<< exit cheese_and_crackers\n")

# make sure that the indentation is removed otherwise python doesn't seem to want to run
# Commented out to try input values below
"""print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)"""

print("We can give the inputs directly into the teminal:\n")

print(f"How many packets of cheese do you have?\n")
cheese = input ()

print(f"How many boxes of crackers do you have?\n")
crackers = input ()

cheese_and_crackers(cheese, crackers)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")

#print(f"How many packets of cheese do you have?")
#cheese = input ()

#print(f"How many boxes of crackers do you have?")
#crackers = input ()

cheese_and_crackers(100 + 10, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
