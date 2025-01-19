# Inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        # Code to start the vehicle
        pass

    def stop(self):
        # Code to stop the vehicle
        pass


class Car(Vehicle):
    def __init__(self, make, model, doors_qty):
        super().__init__(make, model)
        self.doors_qty = doors_qty

    def lock_doors(self):
        # Logic to lick the doors
        pass

    def unlock_doors(self):
        # Logic to unlock doors
        pass