cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
# Deleted copied line 12
print "We can transport", carpool_capacity, "people today." #correction
print "We need to put about", average_passengers_per_car, "in each car."


#Study Drill

#Error explained - Seems he forgot to either put in "car_pool_capacity" or mispelled it.

print "****************** Test Program ****************************"

print "Why does 4.0 + 5", 4.0 + 5

A = 4.0
B = 5

print "Why does A + B", A * B

print "But when I do this", carpool_capacity
