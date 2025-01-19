# Function zip

a = [1, 2, 3, 4, 3, 2]
b = [5, 6, 7, 8, 9, 10]
c = "Python"

# z1, *z2 = zip(a, b, c)
# print(z1,'\n',z2)

z = zip(a, b, c)
# lz = list(z)
# print(*lz)
v = zip(*z)
print(list(v))



# x = zip(a, b, c)
# for i, j, k in x:
#     print(i, j, k)
# print(list(x))