def positiv(a):
    return True if a > 0 else False


z = filter(positiv, [5, -6, -2, 0, 12, 3, -5])
for element in z:
    print(element)

print(type(z))