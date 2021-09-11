from random import shuffle

################################################################################
'''
Some global variables to create cards
These variables contains Suite, Values and Position of cards

'''
suites = ( 'Clubs','Heart','Spade','Diamond' )
positions = ( 'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Joker','Queen','King','Ace' )
values = { 'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Joker':10,'Queen':10,'King':10,'Ace':11 }

################################################################################
'''
A class named Cards is declared to create unique cards by taking input and
relating its according to the value

'''
class Cards():
    def __init__(self, positions, suites):
        self.suites = suites
        self.positions = positions
        self.values = values[positions]

    def __str__(self):
        return self.positions + " of " + self.suites

################################################################################
'''
A class named Deck to initiate the creation of the whole deck and return  it

'''
class Deck():
    def __init__(self):
        self.all_cards = []
        for suite in suites:
            for position in positions:
                card = Cards(position, suite)
                self.all_cards.append(card)
    def add_card(self):
        return self.all_cards.pop()

################################################################################
'''
A class named Player to create player hands attributes
such as -
Hit
Stand
Double Down
class Player():
    def __init__(self):
'''


################################################################################

card_cl = Deck()
deck = []
for x in range(52):
    deck.append(card_cl.add_card())
shuffle(deck)
player = []
comp = []
player_value = 0
comp_value = 0
count = 0
game_on=True
while(game_on == True):
    for x in range(2):
        comp.append(deck.pop())
    for y in range(2):
        player.append(deck.pop())

    print(f"Master's card : {comp[-1]} , 1 Unturned Card")

    print("\nPlayer's card :", end=" ")
    for x in range(len(player)):
        print(player[x], end=" , ")

    print("\n")

    hit = 1
    while(hit==1):
        hit = int(input("Choose : 1.Hit or 2.Stand -  "))
        if hit==1:
            player.append(deck.pop())
            print("\n\nUpdated Player's card :", end=" ")
            for x in range(len(player)):
                print(player[x], end=" , ")
        elif hit==2:
            pass
        else:
            print("\nInvalid Input (please try again)")
            hit = 1

    for x in range(len(player)):
        if(player[x].values==11):
            ans = input("Do you want to assume Ace as 1 ? (y/n) : ")
            if(ans=='y' or ans=='Y'):
                player[x].values = 1
            else:
                pass
        player_value += player[x].values

    if(player_value>21):
        print("\nPlayer lose due to point being more than 21 ")
        game_on = False
        break

    print("\nMaster's card : ",end=" ")
    for y in range(len(comp)):
        print(comp[y],end=" , ")
        comp_value += comp[y].values

    if comp_value<player_value:
        comp.append(deck.pop())
        comp_value+= comp[-1].values

    if comp_value>21:
        for y in range(len(comp)):
            if comp[y].values==11:
                count+=1
        if count>0:
            comp_value-=10
    if(len(comp)>2):
        print("\nUpdated Master's card : ",end=" ")
        for y in range(len(comp)):
            print(comp[y],end=" , ")



    if comp_value>21:
        print("\nComputer lose due to point being more than 21 ")
    elif player_value>comp_value:
        print("\nPlayer WON !!! ")
    elif player_value<comp_value:
        print("\nMaster WON !!! ")
    else:
        print("\nIts a draw !!! ")

    answer= input("\nPress 'y' if you want to play again : ")
    if(answer=='y' or answer=='Y'):
        game_on = True
        for x in range(len(player)):
            deck.append(player.pop())
        for y in range(len(comp)):
            deck.append(comp.pop())
        shuffle(deck)
    else:
        game_on = False
        break
