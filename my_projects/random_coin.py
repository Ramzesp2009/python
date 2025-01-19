import random

def coin_flip():
    if random.randint(0, 1):
        return "heads"
    else:
        return "tails"


heads_tally, tails_tally = 0, 0
for trial in range(10_000):
    if coin_flip() == "heads":
        heads_tally += 1
    else:
        tails_tally += 1


ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")