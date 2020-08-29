import os
import tkinter
from breezypythongui import EasyFrame

class Card(object):
    '''defines the name, suit, value, and img for each card '''
      
    def __init__(self, name, suit, value):            
        self.name = name
        self.suit = suit
        self.value = value
        x = self.suit + self.name
        imgX = 'imgs\\' + x + '.gif'
        self.image = tkinter.PhotoImage(file= imgX )
