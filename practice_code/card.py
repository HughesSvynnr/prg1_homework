

from rank import rank
from suit import suit


class card():
    def __init__(self,peramiter_suit,peramiter_rank):
        r = rank()
        valid_rank = r.validate(peramiter_rank)

        s = suit()
        s.validate(peramiter_suit)

        if(valid_rank and valid_suit):
            self.suit = suit
            self.rank = rank
        else:
            raise ValueError("Invalid Rank or Suit")

    def display(self):
        print(self.rank + " of " + self.suit)


