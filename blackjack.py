import random
print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""        )           
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards=[]
dealer_cards=[]
blackjackcondition=True

def deal_card():
    card=random.choice(cards)
    return card
for _ in range (2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
def score(card):
    if sum(card)==21 and len(card)==2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user_score,dealer_score):
    if user_score==dealer_score:
        return "its a draw nigger"
    elif user_score>dealer_score:
        return "You win on points"
    elif user_score==0:
        return "You got a blackjack you cheeky bastard"
    elif dealer_score==0:
        return "The dealer has a blackjack, put some more money in"
    elif user_score>21:
        return "You went over 21, better luck next time"
    elif dealer_score>21:
        return "You win, Dealer went over 21"
    else:
        return "You lose but remember there are no quitters in this game"

while blackjackcondition==True:

    user_score=score(user_cards)
    dealer_score=score(dealer_cards)

    print(f"Your cards : {user_cards}, current score : {user_score}")
    print(f"Dealers first card : {dealer_cards[0]}")

    if user_score>21 or dealer_score>21 or user_score==0 or dealer_score==0:
        blackjackcondition=False
        print("You lose loser")
    else:

        hit=input("Do you want to draw another card? or pass ")
        if hit=="y":
            user_cards.append(deal_card())
        else:
            blackjackcondition=False

    if dealer_score!=0 or dealer_score<17:
        dealer_cards.append(deal_card())
        computer_score=score(dealer_cards)

print(f"   Your final hand: {user_cards} final score: {user_score}")
print(f"   Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
print(compare(user_score,dealer_score))


