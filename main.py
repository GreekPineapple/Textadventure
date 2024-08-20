import random, globals
from person import Player, Villain
from map import *
from notes import *
map = Map(4,4)
me = Player(200, 10, "myself", [], 42) #Start: Townhall
notes = Notes()
townhall = TownHall()
woods = Woods("open")
wf = Waterfall("open")
dam = Dam("open")
aquarium = Aquarium("open")
square = Square()
birdhouse = BirdHouse("open")
ww = WestWoods()
sw = SouthWoods()
ew = EastWoods()

goblin = Villain("Goblin", 90, 35, [10, 20, 15], "goblin überreste")
golem = Villain("Erdgolem", 140, 50, [20, 20, 10], "golem überreste")
wizard = Villain("Magier", 135, 40,[10, 20, 10], "wizard überreste")
luftGegner = Villain("Luftgegner", 110, 30,[5, 20, 0], "vogel überreste")

boss = Villain("Boss", 150, 150, ["a","b","c"], "special glitzer boss attacke")

villains = [goblin, golem, wizard, luftGegner]
fields = [townhall, woods, wf, dam, aquarium, square, birdhouse, ww, ew, sw]

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
            wf.quest = wf.explore(dam.quest, notes, me)
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

# quest can be: open; active; done; 

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