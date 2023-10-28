import random
class Car:


    brand = "Lexus"
    model = "600d"


    def __init__(self, color, year, mileage, price):
        self.color = color
        self.year = year
        self.mileage = mileage
        self.price = price


    def drive(self):
        print("The car is driving.")

    def stop(self):
        print("The car is stopping.")



car = Car("white", 2023, 0, 150000)




print("car brand is: ", car.brand)
print("car model is: ", car.model)
print("car color is :", car.color)
print("car year is: ", car.year)
print("car millage is: ", car.mileage)


car.drive()
car.stop()