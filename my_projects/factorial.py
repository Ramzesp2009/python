# def factoeial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *=i
#     return result
#
# number = int(input())
# print(f"Factorial {number} is {factoeial(number)}")

i = int(input())
fac = 1
for j in range(i):
    fac = fac * (j + 1)
print(f"Factorial from {i} is {fac}")

# i = int(input())
# fac = 1
# for j in range(1, i + 1):
#     fac *= j
# print(f"Factorial from {i} is {fac}")