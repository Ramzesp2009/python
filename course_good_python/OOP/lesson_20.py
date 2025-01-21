class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    name = "Line"
    def draw(self):
        print("draw line")


class Rect(Geom):
    name = "Rect"
    def draw(self):
        print("draw rectangle")


l = Line()
r = Rect()
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 3, 3)
# r.name = "Rect"

print(l.__dict__)
print(r.__dict__)