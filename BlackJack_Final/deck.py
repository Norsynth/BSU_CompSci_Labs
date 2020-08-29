from card import Card
import random

class Deck():
    '''creates a deck of cards and deals them '''
    def __init__(self):        
        self.deck = self.createDeck()

    def createDeck(self):
        '''Makes a new deck '''
        name = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        value = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        deck = []
        for i in range(len(name)):
            for s in suit:
                v = value[i]
                c = Card(name[i], s, v)
                deck.append(c)
        random.shuffle(deck)
        return deck

    def dealCard(self):
        '''removes the first card in the deck and gives it to whoever calls the function '''
        card = self.deck.pop(0)
        return card
