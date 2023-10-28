import random
    # Первое Задание
class Zoo:


    total_animals = 0
    total_weight = 0


    type = ""
    name = ""
    age = 0
    gender = ""
    weight = 0
    can_fly = False
    can_swim = False

    def __init__(self, type, name, age, gender, weight, can_fly, can_swim):
        self.type = type
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.can_fly = can_fly
        self.can_swim = can_swim


        Zoo.total_animals += 1

        Zoo.total_weight += weight


    def fly(self):
        if self.can_fly:
            print("Flying")
        else:
            print("This animal can't fly")

    def swim(self):
        if self.can_swim:
            print("Swimming")
        else:
            print("This animal can't swim")





lion = Zoo("Lion", "Peter", 10, "Male", 200, True, False)
tiger = Zoo("Tiger", "George", 5, "Male", 150, False, False)
bird = Zoo("Bird", "Kesha", 2, "Male", 10, True, False)
fish = Zoo("Fish", "Anna", 1, "Female", 1, False, True)
crocodile = Zoo("Crocodile", "Gosha", 3, "Male", 1200, False, True)


lion.fly()
tiger.swim()
bird.swim()
fish.swim()
crocodile.fly()

