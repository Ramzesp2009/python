# def mysum(L):
#     print(L)
#     if not L:
#         return 0
#     else:
#         return L[0] + mysum(L[1:])


# def mysum_2(L):
#     return 0 if not L else L[0] + mysum_2(L[1:])

# def mysum_3(L):
#     return L[0] if len(L) == 1 else L[0] + mysum_3(L[1:])

# def mysum_4(L):
#     first, *rest = L
#     return first if not rest else first + mysum_4(rest)
#
# print(mysum_4(['spam', 'spam']))

# def mysum(L):
#     if not L:
#         return 0
#     return nonempty(L)
#
# def nonempty(L):
#     return L[0] + mysum(L[1:])
#
# print(mysum([1.1, 2.2, 3.3, 4.4]))

# L = [1, 2, 3, 4, 5]
# sum = 0
# while L:
#     sum += L[0]
#     L = L[1:]
#
# print(sum)

L = list(range(11))
sum = 0
for i in L:
    sum += i
print(sum)