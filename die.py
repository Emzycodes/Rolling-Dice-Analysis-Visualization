from random import randint
class Die:
    def __init__(self,side=6):
        self.sides = side

    def roll_die(self):
        return randint(1,self.sides)
    
