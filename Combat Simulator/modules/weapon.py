
from die import die

class weapon:
    def __init__(self, name: str, die: die, bonus: int = 0):

        self.name = name
        self.die = die
        self.bonus = bonus
        
    def dmgrolls(self) -> tuple[list[int], int]:

        rolls = self.die.rolls()
        return rolls, self.bonus



longsword = weapon("Longsword", die(2,6), 2)
greatsword = weapon("Greatsword", die(3,8), -2)


