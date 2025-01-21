v1 = [1, 2, 3]
v2 = [7, 6, 5]

class DefenedVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v = self.__temp
        return False

try:
    with DefenedVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Error")

print(v1)