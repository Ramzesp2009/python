# magic method __call__ (dunder-method)
import math


# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, step=1, *args, **kwargs):
#         print("__call__")
#         self.__counter += step
#         return self.__counter
#
#
# c = Counter()
# c_2 = Counter()
# c() # functor
# c(2)
# c_2()
# c_2(-5)
# c()
# res = c(10)
# res_2 = c_2()
# print(res, '/', res_2)

# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("The argument must be string")
#         return args[0].strip(self.__chars)
#
#
# s = StripChars("!:?;/ _-=+")
# res = s(" !!==Pavlo Romazan? _-+=")
# print(res)


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self,x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))
