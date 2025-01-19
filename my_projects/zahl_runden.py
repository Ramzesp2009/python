x = 1.499999
print("x:", round(x))
x = 1.500000
print("x:", round(x))
print()

x = 12/7
print("x:", x)
print("Gerundet auf sechs Stellen nach dem Kemma:", round(x, 6))
print("Gerundet auf null Stellen:", round(x))
print("int(x):", int(x))
print()

x = 12e6/7
print("x:", x)
print("Gerundet auf drei Stellen vor dem Kemma:", round(x, -3))
print("Gerundet auf null Stellen:", round(x))
print("int(x):", int(x))
