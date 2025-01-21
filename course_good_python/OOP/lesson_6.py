from accessify import private, protected

class Point:

    def __init__(self, x=0, y=0):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError ("Coordinates musst be digital")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 12)
print(pt.check_value(5))