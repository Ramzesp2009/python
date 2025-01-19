class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, miles):
        self.mileage = self.mileage + miles


blue_car = Car("blue", 20_000)
red_car = Car("red", 30_000)
blue_car.drive(1000)
red_car.drive(4444)


print(f"The {blue_car.color} car has {blue_car.mileage:,} miles.")
print(f"The {red_car.color} car has {red_car.mileage:,} miles.")
