class Punkt:
    def __init__(self, xk=0.0, yk=0.0):
        self.x = xk
        self.y = yk

    def verschieben(self, xk=0.0, yk=0.0):
        self.x += xk
        self.y += yk

    def __str__(self):
        return f"{self.x} / {self.y}"



punkt1 = Punkt()
print(punkt1)
punkt2 = Punkt(3.5, 2.5)
print(punkt2)
punkt3 = Punkt(4.0)
print(punkt3)
punkt4 = Punkt(yk=1.5)
print(punkt4)
punkt4.verschieben(4.5, 2)
print(punkt4)
