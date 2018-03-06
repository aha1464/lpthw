name = 'Alli H. Archer'
age = 38 # Not a lie
height = 156 # cm
height_inches = 156 / round (2.54) # calculation for conversion to inches
weight = 180 # lbs
weight_kg = 180 / round (2.2)
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'

print(f"Let's talk about {name}.")
print(f"She's {height} cm tall. Which is {height_inches} inches.")
print(f"She's {weight} pounds heavy. Which is {weight_kg} kilograms.")
print("Actually that's not too heavy.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
