dict_cats = {i: 0 for i in range(1, 101)}
n = 1
hats = list(dict_cats.values())
while n <= 100:
    for i in range(n, 101, n):
        dict_cats[i] = 1 if dict_cats[i] == 0 else 0
    n += 1

for key, value in dict_cats.items():
    if value == 1:
        print(key, end=' ')



#
# list_cats = {i: 0 for i in range(1, 101)}
# n = 1
#
# while n <= 100:
#     for i in range(n, 101, n):
#         # Змінюємо стан капелюха у кота
#         list_cats[i] = 1 if list_cats[i] == 0 else 0
#     n += 1
#
# # Виводимо котів, які залишилися з капелюхом
# for key, value in list_cats.items():
#     if value == 1:
#         print(key, end=' ')