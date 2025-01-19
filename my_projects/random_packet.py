import random

print(random.random())

print(random.randint(1, 10))

print(random.choice((1, 2, 3, 4, 5, 6, 7)))

print(random.choices((1, 2, 3, 4, 5, 6, 7), k=2))

my_list = [1, 2, 3, 4, 5, 6, 7]
print(random.shuffle(my_list))
print(my_list)
print(random.shuffle(my_list))
print(my_list)

print(''.join(random.choices('ABCDEF0123456789', k=8)))
