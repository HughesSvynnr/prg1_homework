

from rank import rank
from suit import suit


class card():
    def __init__(self,suit,rank):
        r = rank
        valid_rank = r.validate(rank)

        s = suit()
        s.validate(suit)

        if(valid_rank and valid_suit):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = "Invalid"
            self.rank = "Invalid"

    def display(self):
        print(self.rank + " of " + self.suit)