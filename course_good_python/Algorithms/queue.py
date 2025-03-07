import collections


# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#     print(a.pop(0))
#     print('---'*5)

a = collections.deque([1, 2, 3, 4, 5])
print('---'*5)
for i in range(len(a)):
    print('------', a.popleft(), '------')
    print('---'*5)
