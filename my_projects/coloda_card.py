cards = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'Jack' : 11, 'Queen' : 12, 'King' : 13, 'Ace' : 14}
cards_2 = [input() for card in range(6)]
i = 0
res = 0
while i < len(cards_2):
    if cards_2[i] in cards:
        res += cards[cards_2[i]]
        i += 1
    else:
        print("The cart not exist")
print(res/len(cards_2))

# deck = {str(i): i for i in range(2, 11)}
# deck.update({'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14})
# print(sum(deck[i] for i in [input() for i in range(6)]) / 6)