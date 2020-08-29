'''
This is the main python module.  It houses the GameTable class and functionality.
It imports the card, player, and deck modules for its functionality.
'''
import tkinter
from breezypythongui import EasyFrame


from card import Card
from deck import Deck
from player import Player

class GameTable(EasyFrame):
    '''Class defining the game table and its functions '''

    def __init__(self):
        '''initiates the game table, labels, and buttons '''
        EasyFrame.__init__(self)
        self.setTitle('Black Jack 3000')
        self.setBackground('black')

        #create the game table - use a canvas to force the window to not resize with every new card added to the field.
        self.addCanvas(height=400, width=800, row=0, column=0, rowspan=1, columnspan=4, background='green')
        self.panel = self.addPanel(row=0, column=0, rowspan=1, columnspan=4, background='green')

        #create the player and dealer labels so the player knows which cards are which
        self.panel.addLabel(text='DEALER:', row=0, column=0)
        self.panel.addLabel(text='PLAYER:', row=2, column=0)
        
        #creates the buttons for the table
        self.deal = self.addButton(text='DEAL', row=1, column=0, command=self.deal, state='normal')
        self.hit = self.addButton(text='HIT', row=1, column=1, command=self.hit, state='disabled')
        self.stay = self.addButton(text='STAY', row=1, column=2, command=self.stay, state='disabled')
        self.buttons=[self.deal, self.hit, self.stay]


        #list of labels on the table.  Used to delete them after game is over.
        self.cardsOnTable = []

        #initializes the deck, player, and dealer objects
        self.deck = Deck()
        self.player = Player('Player', self)
        self.dealer = Player('Dealer', self)

       
    def deal(self):
        '''creates a new deck and deals out the cards '''
        self.cleanTable()
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)
        self.player.hit(self.deck)
        self.deal['state'] = 'disabled'
        self.hit['state'] = 'normal'
        self.stay['state'] = 'normal'
        

    def hit(self):
        '''Player takes a card '''
        self.player.hit(self.deck)
        

    def stay(self):
        '''Player ends turn and dealer plays '''
        for b in self.buttons:
            b['state'] = 'disabled'
        self.dealer.play(self.deck)
        self.outcome()
        
             
    def showCards(self):
        '''Displays the player and dealer cards on the table '''
        for i in range(len(self.dealer.hand)):
            lbl = self.panel.addLabel(text='', row=1, column=i, sticky='NW')
            lbl['image'] = self.dealer.hand[i].image
            self.cardsOnTable.append(lbl)
        for j in range(len(self.player.hand)):
            lbl = self.panel.addLabel(text='', row=3, column=j, sticky='NW')
            lbl['image'] = self.player.hand[j].image
            self.cardsOnTable.append(lbl)
        

    def cleanTable(self):
        '''clears and cards from the table and empties the player hands '''
        for c in self.cardsOnTable:
            c.destroy()
        self.player.hand = []
        self.dealer.hand = []
        del self.deck #delete the old deck before making a new one to prevent memory leak issues.
        self.deck = Deck()
        
    def message(self, message):
        '''Displays a message on screen '''
        self.messageBox(message=message)
        self.deal['state'] = 'normal'
        self.hit['state'] = 'disabled'
        self.stay['state'] = 'disabled'

    def outcome(self):
        '''Determines the outcome of the game '''
        if self.player.score2 == self.dealer.score:
            self.message('Push')
        elif self.player.score2 > self.dealer.score:
            self.message('Player wins!')
        elif self.dealer.score > self.player.score2 and self.dealer.score <= 21:
            self.message('Dealer wins!')
        self.deal['state']='normal'
        
def main():
    g = GameTable()

if __name__ == '__main__':
    main()
