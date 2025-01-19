import math


class Point3D:
    def __init__(self, coord_x, coord_y, coord_z):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z

    def __add__(self, other):
        self.coord_x += other.coord_x
        self.coord_y += other.coord_y
        self.coord_z += other.coord_z
        return self.coord_x, self.coord_y, self.coord_z

    def __sub__(self, other):
        self.coord_x -= other.coord_x
        self.coord_y -= other.coord_y
        self.coord_z -= other.coord_z
        return self.coord_x, self.coord_y, self.coord_z

    def __eq__(self, other):
        return (self.coord_x == other.coord_x and
                self.coord_y == other.coord_y and
                self.coord_z == other.coord_z)

    def __abs__(self):
        return math.sqrt(self.coord_x ** 2 + self.coord_y ** 2 + self.coord_z ** 2)