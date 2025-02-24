import random, globals
from init_game import *

def checkAction(position):
    match position:
        case 11:
            ww.explore(me, villains, boss)
        case 12:
            pass
        case 13:
            pass
        case 22:
            woods.quest = woods.explore(birdhouse.quest, notes)
        case 23:
            dam.quest = dam.explore(wf.quest, aquarium.quest, me, notes)
        case 30:
            birdhouse.quest = birdhouse.explore(aquarium.quest, woods.quest, notes)
        case 31:
            aquarium.quest = aquarium.explore(dam.quest, birdhouse.quest, me, notes)
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

map.printMap(fields)
notes.read()

block = False # avoids two fights after another

while me.lives > 0:
    if globals.winning:
        print("Yaay du hast gewonnen")
        break
    print("Was möchtest du machen?")
    doing = input(">").lower().strip()
    if doing == "umschauen":
        block = lookAround(block)
    elif doing == "laufen":
        me.move(wf.quest)
        printposition(me.positionNow)
    elif doing == "inventar":
        print(me.inventory)
    elif doing == "help":
        notes.read()
    elif doing == "map":
        map.printMap()
    elif doing == "ende":
        break
    else:
        print("ungültige eingabe")
print("GAME OVER!")