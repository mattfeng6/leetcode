# https://www.w3schools.com/python/python_arrays.asp

# Array
# e.g.
cars = ["Ford", "Volvo", "BMW"]

# Access & Modify the Array
car1 = cars[0]
cars[0] = "Toyota"

# Length of an Array
length = len(cars)

# Looping Array Elements
for car in cars:
    print(car)

# Adding Array Elements
cars.append("Honda")

# Removing Array Elements
cars.pop(0)
cars.remove("Volvo")