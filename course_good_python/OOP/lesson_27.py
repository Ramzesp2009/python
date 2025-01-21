class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5


class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

