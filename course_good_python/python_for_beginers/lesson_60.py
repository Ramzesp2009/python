# def is_odd(x):
#     return x % 2

def key_sort(x):
    return x if x % 2 == 0 else 100 + x


a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x % 2)
print(a)
b = sorted(a, key=key_sort)
print(b)