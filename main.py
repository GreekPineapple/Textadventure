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

def checkaction(position): #TODO mach match-case draus
    if position == 11: # Wald
        ww.explore(me, villains, boss)
    elif position == 12: # Wald
       pass
    elif position == 13: # Wald
       pass
    elif position == 22: # Wald
        woods.quest = woods.explore(birdhouse.quest, notes)
    elif position == 23: # Staudamm
        dam.quest = dam.explore(wf.quest, aquarium.quest, me, notes)
    elif position == 30: # Vogelhaus
        birdhouse.quest = birdhouse.explore(aquarium.quest, woods.quest, notes)
    elif position == 31: # Aquarium
        aquarium.quest = aquarium.explore(dam.quest, birdhouse.quest, me, notes)
    elif position == 32: # Dorfplatz
        square.explore(me)
    elif position == 33: # Wasserfall
        wf.quest = wf.explore(dam.quest, notes, me)
    elif position == 42: # Rathaus
        townhall.explore(me)
    else:
        print("You're out of map lul")

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
        checkaction(me.positionNow)
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