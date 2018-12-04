import random
from card import card
from rank import rank
from suit import suit
class deck():
    def __init__(self,new_deck=False,cards=None):
        if(cards is None): # PYTHON WHY????????????
            cards = []
            self.cards = cards
        if(new_deck):
            for r in rank:
                for s in suit:
                    ranks = rank()
                    suits = suit()
            for s in suits.values:
                for r in ranks.values:
                    c = card(s,r)
                    
                    self.cards.append(c)
             #make a bunch of cards
            #add to self.cards
    
    def cut(self):
        first_half = self.cards[cut_position:]
        second_half = self.cards[:cut_position]
        deck1 = deck(first_half)
        deck2 = deck(second_half)
        deck1 = deck(False,first_half)
        deck2 = deck(False,second_half)
        self.cards = []
        return deck1,deck2
    def split(self):
        cut_position = int(len(self.cards)/2)
        first_half = self.cards[cut_position:]
        second_half = self.cards[:cut_position]
        deck1 = deck(first_half)
        deck2 = deck(second_half)
        deck1 = deck(False,first_half)
        deck2 = deck(False,second_half)
        return deck1,deck2
        return deck1,deck2
    def fan(self):
        pass
        for c in self.cards:
            c.display()