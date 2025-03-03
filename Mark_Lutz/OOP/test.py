class Sun:
    n = True  # number of instances of this class

    def __new__(cls):
        if cls.n:
            cls.n = False
            return object.__new__(cls)
        else:
            return "It isn't possible to create 2 instances"

    def __str__(self):
        return "It's an object of class Sun"


s1 = Sun()
s2 = Sun()
print(s1)
print(s2)