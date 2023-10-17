

playerlist = []

class player:
    def __init__(self, name, weapon, maxhp = 20,):

        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = weapon
                
    def __str__(self):
        return f"{self.name} has {self.hp}/{self.maxhp} HP!"
    
    def attack(self, target):
        rolls = self.weapon.dmgroll()
        dmg = sum()
        if dmg >= target.hp:
            target.hp = 0
        else:
            target.hp -= dmg
            
        return f"{self.name} dealt"
        

