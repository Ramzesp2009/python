class Geom:
    name = 'Geom'
    def __init__(self, x1, y1, x2, y2):
        print(f"Initialization Geom for {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('draw line')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self.fill = fill
        print("Initialization Rectangle")

    def draw(self):
        print('draw rectangle')


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4, )
print(r.__dict__)
