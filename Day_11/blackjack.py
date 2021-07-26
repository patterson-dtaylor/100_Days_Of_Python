import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_total = 0
dealer_total = 0
hit_me = True
dealer_ready = False

def the_play():
    for i in range(0, 2):
        player_hand.append(random.choice(CARDS))
        dealer_hand.append(random.choice(CARDS))

def adding_totals(hand):
    hand_total = 0
    for card in hand:
        hand_total += card
    return hand_total

# def hit_me()

def check_for_aces(hand):
    new_hand = []
    for card in hand:
        if card == 11:
            card = 1
            new_hand.append(card)
        else:
            new_hand.append(card)
    return new_hand

the_play()
player_total = adding_totals(player_hand)
dealer_total = adding_totals(dealer_hand)
print(f"Player's hand: {player_hand}")
print(f"Dealer's hand: {dealer_hand}")

while dealer_ready == False:
    if dealer_total < 17:
        dealer_hand.append(random.choice(CARDS))
        dealer_total = adding_totals(dealer_hand)
        print(f"Dealer's hand: {dealer_hand}")
    elif dealer_total >= 17:
        dealer_ready = True

# FIXME: When ace is pulled and over 21 it needs to change to 1.
while hit_me:
    hit_or_stand = input("Player, would you like to hit or stay? (hit/stay) ")
    if hit_or_stand == "hit":
        if 11 in player_hand:
            for card in player_hand:
                if card == 11:
                    card = 1
            player_total = adding_totals(player_hand)
            player_hand.append(random.choice(CARDS))
            player_total = adding_totals(player_hand)
            
        else:
            player_hand.append(random.choice(CARDS))
            player_total = adding_totals(player_hand)
            print(f"Player's hand: {player_hand}")
        
        if player_total > 21:
            print(f"Player busted...")
            print("House wins...")
            break
    elif hit_or_stand == "stay":
        if dealer_total > 21 or player_total > dealer_total:
            print("Player wins!")
            print(f"Player's hand: {player_hand}")
            print(f"Dealer's hand: {dealer_hand}")
        elif dealer_total <= 21 and player_total < dealer_total:
            print("House wins...")
            print(f"Player's hand: {player_hand}")
            print(f"Dealer's hand: {dealer_hand}")
        elif dealer_total == player_total:
            print("Draw...")
        hit_me = False



