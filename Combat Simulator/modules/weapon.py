
import modules.special as special

class weapon:
    def __init__(self, name, amount = 1, die = 6, bonus = 0, special = "", specialchance = 0):

        self.name = name
        self.die = die
        self.amount = amount
        self.bonus = bonus
        self.range = f"{self.amount + self.bonus}-{self.amount * self.die + self.bonus}"
        self.special = special
        self.specialchance = specialchance

    def __str__(self):
        if self.special == "":
            return f"\n{self.name}: \nAttack: {self.amount}d{self.die}+{self.bonus} ({self.range})\nSpecial Effekt: None"
        else:
            return f"\n{self.name} \nAttack: {self.amount}d{self.die}+{self.bonus} ({self.range})\nSpecial Effekt: {self.specialchance}% {self.special}"
    


longsword = weapon("Longsword", 1, 8, 2)
greatsword = weapon("Greatsword", 2, 6)
mace = weapon("Mace", 1, 4, 1, special.stun, 50)


