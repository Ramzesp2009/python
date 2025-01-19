import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = [ "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

list_nouns = []
list_verbs = []
list_adjectives = []
list_prepositions = []
list_adverbs = []

for i in range(3):
    list_nouns.append(random.choice(nouns))

for i in range(3):
    list_verbs.append(random.choice(verbs))

for i in range(3):
    list_adjectives.append(random.choice(adjectives))

for i in range(2):
    list_prepositions.append(random.choice(prepositions))

for i in range(1):
    list_adverbs.append(random.choice(adverbs))

print(f'A {list_adjectives[0]} {list_nouns[0]}')
print()
print(f'A {list_adjectives[0]} {list_nouns[0]} {list_verbs[0]} {list_prepositions[0]} '
      f'the {list_adjectives[1]} {list_nouns[1]}')
print(f'{list_adverbs[0]}, the {list_nouns[0]} {list_verbs[1]}')
print(f'the {list_nouns[1]} {list_verbs[2]} {list_prepositions[1]} a '
      f'{list_adjectives[2]} {list_nouns[2]}')

random.sample()