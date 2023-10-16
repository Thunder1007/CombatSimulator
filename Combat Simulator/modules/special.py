
import random
import time

class special:
    def __init__(self, name = "", func = "", type = 0):
        self.name = name
        self.func = func
        self.type = type

    def __str__(self) -> str:
        return self.name

def doStun(chance, applier, target = ""):

    if chance >= random.randint(1,100):

        target.conditions.append("applyStun")
        time.sleep(1.5)
        print(f"{applier.name} has stunned {target.name} with his {applier.weapon.name} ({chance}% Chance)!")
        time.sleep(2.5)
        print(f"{target.name} can't attack next round!\n")
        time.sleep(2)


stun = special("Stun-Chance on Hit", doStun, "OnHit")

