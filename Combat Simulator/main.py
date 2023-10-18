

from modules.game import game
from modules.player import *
from time import sleep

playerlist = []

p1 = player("Felix", longsword, 20)
p2 = player("Sönke", greatsword, 20)


game1 = game()
game1.runGame(p1, p2)

def out(str: str):

    print(str)
    sleep(1)

for turn in game1.gamelog:
    for event in turn:
        out(event)