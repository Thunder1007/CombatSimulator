
import modules.weapon as weapon
import modules.special as special

playerlist = []

class player:
    def __init__(self, name, weapon, maxhp = 20,):

        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = weapon
        self.conditions = []
        self.hasAttacked = False


                
    def __str__(self):
        return f"{self.name} now has {self.hp}/{self.maxhp} HP!"
        


p1 = player("Sönke", weapon.mace)
playerlist.append(p1)

p2 = player("Felix", weapon.longsword)
playerlist.append(p2)
