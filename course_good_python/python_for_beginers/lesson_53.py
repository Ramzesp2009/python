import pickle

book1 = ["lksdfjlj", "lsdjf", 100]
book2 = ["lksdfjlj", "lsdjf", 100]
book3 = ["lksdfjlj", "lsdjf", 100]
book4 = ["lksdfjlj", "lsdjf", 100]

try:
    with open("../out.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except:
    print("ERROR")

print(b1)
print(b2)
print(b3)
print(b4)