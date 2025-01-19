flags = 5
mask = 4
res = flags & mask
# print(res)

flags = 13
mask = 5
flags = flags & ~mask
# print(flags)

f = 8
m = 5
f = f | m
# print(f)

f = 9
m = 1
f = f ^ m
print(f)