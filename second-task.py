import random
class Car:

    # Class attributes
    brand = "Lexus"
    model = "600d"

    # Object attributes
    def __init__(self, color, year, mileage, price):
        self.color = color
        self.year = year
        self.mileage = mileage
        self.price = price

    # Methods
    def drive(self):
        print("The car is driving.")

    def stop(self):
        print("The car is stopping.")


# Create a car object
car = Car("white", 2023, 0, 150000)




print("car brand is: ", car.brand)
print("car model is: ", car.model)
print("car color is :", car.color)
print("car year is: ", car.year)
print("car millage is: ", car.mileage)

# Call the car's methods
car.drive()
car.stop()