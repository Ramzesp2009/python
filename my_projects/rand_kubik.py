import random

def rand_kubik():
    side_of_kubik = random.randint(1, 6)
    return side_of_kubik


total_sume = 0
for mal in range(10_000):
    total_sume += rand_kubik()
print(total_sume / 10_000)