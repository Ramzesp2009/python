data = (4.5, 8.7, True, 'book', 8, 10, -11, [True, False])

s = sum(filter(lambda x: isinstance(x, float), data))

# s = 0
# for x in data:
#     if isinstance(x, float):
#         s += x

print(s)