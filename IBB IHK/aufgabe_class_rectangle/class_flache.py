class Flache:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return  f"Flache ist ({self.height}, {self.width})"

    def __mul__(self, other):
        return self.width * other, self.height * other