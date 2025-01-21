# function filter

def is_prost(x):
    d = x - 1
    if d < 0 or x % 2 == 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = filter(is_prost, a)
print(list(b))
# b2 = filter(lambda x: x % 2 != 0, b)
#
# b3 = filter(lambda x: x % 2 != 0, filter(is_prost, a))
#
# print(list(b2))

# for i in b:
#     print(i, end=' ')
# print(next(b))

# lst = tuple(b)
# print(lst)
# for i in lst:
#     print(i, end=' ')