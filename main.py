import random, globals
from init_game import *

def checkAction(position):
    match position:
        case 11:
            ww.explore(me, villains, boss)
        case 12:
            woods.explore(berndTheBird)
        case 13:
            pass
        case 22:
            pass
        case 23:
            dam.explore(me, inge)
        case 30:
            birdhouse.explore(tom)
        case 31:
            aquarium.explore(me, aquilina)
        case 32:
            square.explore(me)
        case 33:
            wf.explore(me, rainer)
        case 42:
            townhall.explore(me)

def printposition(position):
    for field in fields:
        if field.number == position:
            print(f"--{field.name.strip()}--")

def lookAround(block):
    fight = random.choices((True, False), weights = [1, 3])
    if fight[0] and not block:
        villain = random.choice(villains)
        villain.printInfo()
        if input("Nimmst du den Kampf an?").lower().strip() == "ja":
            me.fight(villain)
        block = not block
    else:       
        checkAction(me.positionNow)
        block = not block
    return block

init_game.loadquests()

map.printMap(fields)
notes.read()

block = False # avoids two fights after another

while me.lives > 0:
    if globals.WINNING:
        print("Yaay du hast gewonnen")
        break
    print("Was möchtest du machen?")
    doing = input(">").lower().strip()
    if doing == "umschauen":
        block = lookAround(block)
    elif doing == "laufen":
        me.move(inge.quest.state)
        printposition(me.positionNow)
    elif doing == "inventar":
        me.inventory = +me.inventory
        print(str(me.inventory).replace("Counter", "Dein Inventar: "))
    elif doing == "help":
        notes.read()
    elif doing == "map":
        map.printMap(fields)
    elif doing == "ende":
        break
    else:
        print("ungültige eingabe")
print("GAME OVER!")