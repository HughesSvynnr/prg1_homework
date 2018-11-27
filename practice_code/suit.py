class suit():
    def __init__(self,suit_value):
        self.values = {
            "heart":0,
            "spade":1,
            "diamond":2,
            "clubs":3,
            "invalid":-1
        }
    def validate(self, suit_value):
        if(suit_value in self.values):
            return True
        else:
            return False