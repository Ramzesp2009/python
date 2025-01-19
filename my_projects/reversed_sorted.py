t = 4, 12, 6, -2
print("Tupel:", t)
print("Umgedreht: ", end="")
for i in reversed(t):
    print(i, end=" ")
print()
print("Sortiert:", sorted(t))
print()
dc = {"Peter":32, "Julia":28, "Werner":35}
print("Dictionary:", dc)
va = dc.values()
vk = dc.keys()
print("Keys-View:", vk)
print("Werte-View:", va)
print("Umgedreht: ", end="")
print(i for i in reversed(vk))
# for i in reversed(vk):
#     print(i, end=" ")
print()
print("Sortiert:", sorted(vk))
for i in reversed(va):
    print(i, end=" ")
print()
print("Sortiert:", sorted(va))