from weapon import *
class player:
    def __init__(self, name: str, weapon: weapon, maxhp: int = 20):

        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = weapon
                
    def __str__(self):

        return f"{self.name} has {self.hp}/{self.maxhp} HP!"
    
    def attack(self, target):

        (rolls, bonus) = self.weapon.dmgrolls()
        dmg = sum(rolls) + bonus

        if dmg < 0:
            dmg = 0

        if dmg >= target.hp:
            target.hp = 0
        else:
            target.hp -= dmg
            
        rolltext = ','.join(list(map(lambda x: str(x), rolls)))

        return f"{self.name} dealt {dmg} ([{rolltext}] +{bonus}) damage to {target.name} with his {self.weapon.name}!"
    
    def getHP(self):

        return f"{self.name} now has {self.hp}/{self.maxhp} HP!"

    


