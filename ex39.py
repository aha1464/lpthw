# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some citied in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('-' * 10) # prints out 10 dashes
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# Print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Folrida's abbreviation is: ", states['Florida'])

# Do it by using the state then the cities dict(tionary)
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# Print every abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# Safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# Get clarity with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
