figur = int(input("Enter a positive integer: "))
for i in range(1, figur + 1):
    if figur % i == 0:
        print(f"{i} a factor of {figur}")
    else:
        continue