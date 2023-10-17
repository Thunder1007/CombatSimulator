

from modules.game import *
from modules.player import *

playerlist = []

p1 = player("Felix", longsword, 20)
p2 = player("Sönke", greatsword, 20)
playerlist.append(p1, p2)

game1 = game()
game1.runGame(playerlist)
