# Polymorphism
import math

class Shape:
    def calc_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * pow(self.radius, 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(10, 2), Circle(7), Rectangle(25, 15)]

for shape in shapes:
    print(shape.calc_area())