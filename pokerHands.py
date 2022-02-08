import sys
#Reference: https://deck-of-cards.readthedocs.io/en/latest/
from deck_of_cards import deck_of_cards
#Reference: https://pypi.org/project/names/
import names
import time

class Player:
    name = ''
    cardDeck = None
    #init
    def __init__(self, name):
        self.name = name
    #get name
    def getName(self):
        return self.name
    #get the card deck
    def getCards(self):
        return self.cardDeck
    #add a card in the deck
    def addCard(self, card):
        if self.cardDeck is None:
            self.cardDeck = [card]
        else:
            self.cardDeck.append(card)


#gets the players names
def getPlayerNames(playersList):
    returnNames = []
    for name in playersList:
        returnNames.append(name.getName())
    return returnNames

#Where the game lives
def pokerGameStart(deck, playersList):
    print('Each player will now get one card twice going clockwise\n')
    time.sleep(1)
    for i in range(0, len(playersList)*2):
        playersList[i%len(playersList)].addCard(deck.give_random_card())
        print("Card given to " + playersList[i%len(playersList)].getName())
        time.sleep(.5)
    return 
if __name__=="__main__":
    #gathering all the information needed
    name = input('What is your name? ')
    numberOfPlayers = int(input('How many players are playing? Including yourself (1-4) '))
    while numberOfPlayers < 1 and numberOfPlayers > 4:
        numberOfPlayers = input('''
            Invalid number of players:
            How many players are playing? Including yourself (1-4)
            ''')
    playersList = []
    playersList.append(Player(name))
    for i in range(1, numberOfPlayers):
        playersList.append(Player(names.get_first_name()))
    #to make it an even game, a multiple of x players will determine the appropriate pool of money 
    print("Players tonight are: " + str(getPlayerNames(playersList)))
    print('There will be $' + str(numberOfPlayers*numberOfPlayers*100) + ' in this pool, and will be divided among the ' +
            str(numberOfPlayers) + ' of you all, and it will all be converted into chips. In total, you will start off with $' +
            str(numberOfPlayers *100))
    #Starting a game
    #deck that the dealer will use, the dealer will not play. 
    deck = deck_of_cards.DeckOfCards()
    #shuffling the deck
    print("\nShuffling deck! ")
    for i in range(0,3):
        time.sleep(1)
        print("Shuffling...")
    deck.shuffle_deck()
    print("Shuffled, we can begin the game now. ")
    pokerGameStart(deck, playersList)
    
