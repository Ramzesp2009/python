# modeling a Farm

class Animal():
    amount = 0
    speed_eating = 0
    def __init__(self, breed, age, food, weight):
        self.breed = breed
        self.age = age
        self.food = food
        self.weight = weight

    def __str__(self):
        return f"I'm the {self.breed} and my weight is {self.weight}"

    def eat(self):
        return f"I'll eat it in a {self.amount / self.speed_eating} hour"

class Axel(Animal):
    pass
# def eat(self, amount, speed_eating):

class Cow(Animal):
    pass
class Horse(Animal):
    pass

axel_rick = Axel("Axel", 11, "hay", 350)
axel_rick.eat()
print(axel_rick.eat(200, 23))