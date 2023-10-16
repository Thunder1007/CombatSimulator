
import modules.player as player
import time
import random


roundtimer = 0


def isAlive(list = [player.playerlist]) -> bool:

    for x in list:
        if x.hp == 0:            
            return False
    
    return True


def hasHitEffect(attacker) -> bool:

    if attacker.weapon.special != "":
        if attacker.weapon.special.type == "OnHit":
            return True

    return False


def getHP(*args) -> int:

    for i in args:
        print(f"{i.name} has {i.hp}/{i.maxhp} HP!")
        time.sleep(2)

        if i.hp == 0:
            print(f"{i.name} is dead!")
            time.sleep(2)


def calcDamage(player) -> int:

    total = 0
    damage = 0
    throws = 0

    while throws < player.weapon.amount:
        throws += 1
        damage = random.randint(1, player.weapon.die)
        print(f"Throw {throws}/{player.weapon.amount} (1d{player.weapon.die}): {damage}")
        total += damage
        time.sleep(2)
    
    if player.weapon.bonus != 0:

        print(f"Bonus Damage: {player.weapon.bonus}")
        total += player.weapon.bonus

        time.sleep(2)

    print(f"Total Damage: {total}")
    time.sleep(2)

    if total > 0:
        return total
    else:
        return 0


def startRoundApply(list = player.playerlist) -> None:

    for i in list:
        if "applyStun" in i.conditions:
            i.conditions.append("stunned")
            i.conditions.remove("applyStun")


def endRoundApply():
    pass


def resetConditions(list =player.playerlist) -> None:

    for i in list:
        i.conditions.clear()


def attack(attacker, target) -> None:

    print(f"Damage Calculation for {attacker.name}:")
    time.sleep(2)
    dmg = calcDamage(attacker)

    print(f"\n{attacker.name} dealt {dmg} damage to {target.name} with his {attacker.weapon.name}!\n")
    time.sleep(2)

    if target.hp >= dmg:
        target.hp -= dmg
    else:
        target.hp = 0

    if hasHitEffect(attacker):
        attacker.weapon.special.func(attacker.weapon.specialchance, attacker, target)


def turn(attacker, target) -> None:

    if "stunned" in attacker.conditions:
        print(f"{attacker.name} was Stunned and couldn´t attack this turn!\n")
        attacker.conditions.remove("stunned")
        
    else:
        attack(attacker, target)

    time.sleep(2)


def round() -> None:   
    global roundtimer
    roundtimer += 1
    print(f"\nRound {roundtimer}!")

    time.sleep(1.5)

    print(f"{player.p1.name} & {player.p2.name} attack each other!\n") #If statement bei stun hier einfügen!
    time.sleep(2)

    startRoundApply()
    turn(player.p1, player.p2)
    turn(player.p2, player.p1)

    endRoundApply()

    getHP(player.p1, player.p2)




def getWinner(playerA: player, playerB: player) -> None:

    if playerA.hp == 0 and playerB.hp == 0:
        print("\nBoth players died on the same round.")
        time.sleep(2)
        print("Draw!")

    elif playerB.hp == 0 and playerA.hp != 0:
        print(f"\n{playerA.name} has slain {playerB.name} with his mighty {playerA.weapon.name}!")
        time.sleep(1)
        print("Congratulations!")

    elif playerB.hp != 0 and playerA.hp == 0:
        print(f"\n{playerB.name} has slain {playerA.name} with his mighty {playerB.weapon.name}!")
        time.sleep(1)
        print("Congratulations!")

    else: 
        print("\nRound Limit reached!")
        time.sleep(1)
        print("\nWinner due to Tie-Breaker is...")
        time.sleep(1.5)

        if playerA.hp > playerB.hp:
            print(f"{playerA.name}!")
            time.sleep(1)
            print("Congratulations!")

        elif playerA.hp < playerB.hp:
            print(f"{playerB.name}!")
            time.sleep(1)
            print("Congratulations!")

        else:
            print(f"Noone! Both {playerA.name} & {playerB.name} have {playerA.hp} HP left!")
            time.sleep(2)
            print("Draw!")


def main() -> None:
    
    player.p1.hp = player.p1.maxhp
    player.p2.hp = player.p2.maxhp

    time.sleep(2)
    print(f"\n{player.p1.name} has {player.p1.hp}/{player.p1.maxhp} HP & has the following weapon:\n{player.p1.weapon}")
    time.sleep(3)
    print(f"\n{player.p2.name} has {player.p2.hp}/{player.p2.maxhp} HP & has the following weapon:\n{player.p2.weapon}")
    time.sleep(3)

    while isAlive(player.playerlist) == True and roundtimer < 10:
        round()
    
    print("Combat has concluded!")
    time.sleep(2)
    getWinner(player.p1, player.p2)
    time.sleep(1)

    resetConditions(player.playerlist)
    

main()

