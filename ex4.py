# The next 4 lines are the data that needs to be used for the later calculations.
cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
# General info to give defnition i.e. cars_not_driven equals the number of cars - the number of drivers.
cars_not_driven = cars - drivers
# The number of cars driven has to equal the number of drivers.
cars_driven = drivers
# Total number of people that can be carpooled.
carpool_capacity = cars_driven * space_in_a_car
# average calucation total number of passangers divided by the number of cars_driven.
average_passengers_per_car = passangers / cars_driven

# the "are used to show the text to wrap around" , the number to be pulled from the above info, i.e cars = 100.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("Ther will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passangers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
