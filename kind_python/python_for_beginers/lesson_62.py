# a = [True, True, False, True, True]
a = [1, 1, 1, 0, 1, 2]

# b = all(a)
# print(b)

# all_res = True
# for x in a:
#     all_res = all_res and bool(x)

all_res = False
for x in a:
    all_res = all_res or bool(x)

print(all_res)