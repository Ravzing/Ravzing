import random

deck = []

def create_deck():
    for suit in ["S","H","C","D"]:
        for card in range(2,15):
            deck.append((card,suit))
            
def draw_card(player):
    card = deck[0]
    deck.remove(deck[0])
    print(player + " drew the " + str(card))
    return card
    
def game_rules():
    while True:
        player_one = draw_card("player one")
        player_two = draw_card("player two")
        if player_one[0] > player_two[0]:
            winner = "player one"
        elif player_one[0] < player_two[0]:
            winner = "player two"
        else: 
            winner = "tie"
            
        print(winner + " win")
        
        if len(deck) == 0:
            print("deck is empty")
            break
def main():
    create_deck()
    random.shuffle(deck)  
    game_rules()
    
if __name__=="__main__":
    main()