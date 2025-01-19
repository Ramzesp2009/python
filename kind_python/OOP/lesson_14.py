from tinycss2.ast import AtRule


class Clock:
    __DAY = 86480

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be integer")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("The right operand must be integer or class instance")

        # sc = other
        if isinstance(other, Clock):
            other = other.seconds
        return Clock(self.seconds + other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("The right operand must be integer or class instance")

        if isinstance(other, Clock):
            other = other.seconds

        self.seconds += other
        return self


c1 = Clock(1000)
c1 += 100
print(c1.get_time())
