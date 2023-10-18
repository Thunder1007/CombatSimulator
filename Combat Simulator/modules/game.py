

from turn import *
from player import *



class game:
    def __init__(self, playerlist):

        self.playerlist = playerlist
        self.turn = 0

    def allAlive(self):
    
        for player in self.playerlist:
            if player.hp == 0:
                return False

        return True    

    def runGame(self):
        

        while self.allAlive():
            
            thisturn = turn(1)
