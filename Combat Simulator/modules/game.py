

from turn import *
from player import *



class game:
    def __init__(self, player1 = player, player2 = player):

        self.p1 = player1
        self.p2 = player2
        self.turncount = int(0)
        self.gamelog = []

    def allAlive(self):
    
        if self.p1.hp == 0 or self.p2.hp == 0:
                return False

        return True  
      
    def doTurn(self):

        self.turncount += 1

        thisTurn = turn(self.turncount)

        thisTurn.turnlog.append(f"Turn {self.turncount}!")

        thisTurn.turnlog.append(self.p1.attack(self.p2))
        thisTurn.turnlog.append(self.p2.attack(self.p1))

        thisTurn.turnlog.append(self.p1.getHP())
        thisTurn.turnlog.append(self.p2.getHP())
        
        self.gamelog.append(thisTurn)


    def runGame(self):
        
        while self.p1.hp != 0 or self.p2.hp != 0:
            self.doTurn()