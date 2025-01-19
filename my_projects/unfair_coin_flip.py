import random

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"


heads_tally, tails_tally = 0, 0

for trial in range(10_000):
    if unfair_coin_flip(.7) == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")