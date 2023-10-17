
import random

class weapon:
    def __init__(self, name, amount = 1, die = 6, bonus = 0):

        self.name = name
        self.die = die
        self.amount = amount
        self.bonus = bonus

        def checkAmount(self):
            if self.amount >= 1:
                return True
            else:
                return False
        
        def dmgroll():
            rolls = []
            
            while checkAmount():
                rolls.append(random.randint(1, self.die))
            
            return rolls

