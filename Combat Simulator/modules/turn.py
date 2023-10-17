

from player import *
class turn():
    def __init__(self, number) -> None:
        
        self.number = number
        self.combatlog = []

    def doTurn(self, player):

        self.combatlog.append(f"Turn {self.number}!")

        self.combatlog.append(p1.attack(p2))
        self.combatlog.append(p2.attack(p1))

        for player in playerlist:

            self.combatlog.append(player.getHP())

        
        
        
        