import random

suit = ["S","H","C","D"]

deck = []

for suit in suit:
    for card in range(2,15):
        deck.append((card,suit))

random.shuffle(deck)        
print(deck)