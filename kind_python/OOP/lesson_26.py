import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


p = Point(1, 2)
p2 = Point2D(10, 20)

print(timeit.timeit("p.calc()", setup="from __main__ import p", number=1000000))
print(timeit.timeit("p2.calc()", setup="from __main__ import p2", number=1000000))
print()
t1 = timeit.timeit(p.calc)
t2 = timeit.timeit(p2.calc)
print(t1, t2, sep='\n')