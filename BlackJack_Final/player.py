class Player(object):
    '''Creates the player and dealer obejects and handles behaviour '''
    def __init__(self, name, owner):
        '''initial stats for the player '''
        self.name = name
        self.owner = owner
        self.hand = []
        self.score = self.calcScore()
        self.score2 = 0
        

    def hit(self, deck):
        '''gives a card from the deck to the player hand '''
        c = deck.dealCard()
        self.hand.append(c)
        self.owner.showCards()
        self.calcScore()
        self.checkScore()  

    def calcScore(self):
        '''Calculate the score of the player hand '''
        total =0
        for c in self.hand:
            total+=c.value
        self.score = total
        self.score2 = self.score
        
        
    def play(self, deck):
        '''Rules for if the dealer decides to hit or stay '''
        while self.score < 17:
            self.hit(deck)

    def checkScore(self):
        '''Checks the player score, if over 21, sends a bust message back to the app '''
        for c in self.hand:
            if c.value == 1:
                self.score2 = self.score + 10
        if self.score2 > 21:
            self.score2 = self.score
        if self.score > 21 and self.score2 > 21:
            message = self.name + ' BUSTS'
            self.owner.message(message)
        
