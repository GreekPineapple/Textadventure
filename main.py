import random
from person import Player, Villain
from map import *
from notes import *
map = Map(4,4)
me = Player(200, 40, "myself", [], 42) #Start: Townhall
townhall = TownHall()
woods = Woods("open")
wf = Waterfall("open")
dam = Dam("open")
aquarium = Aquarium("open")
square = Square()
birdhouse = BirdHouse("open")
notes = Notes()

#the smaller the resistance, the smaller the damage (Muss vielleicht *-1 machen, damit sprachlich sinn ergibt xD)
goblin = Villain("Goblin", 100, 50, 1, [5, 0, 10], "goblin überreste")
golem = Villain("Erdgolem", 150, 20, 4, [20, 15, 10], "golem überreste")
wizard = Villain("Magier", 120, 40, 6, [5, 10, 15], "wizard überreste")
luftGegner = Villain("Luftgegner", 110, 25, 2, [5, 20, 0], "vogel überreste")

boss = Villain("Boss", 150, 150, 15, ["a","b","c"], "special glitzer boss attacke")

villains = [goblin, golem, wizard, luftGegner]

def checkaction(position): #TODO mach match-case draus
    if position == 11: # Wald
        pass
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
        pass
    elif position == 33: # Wasserfall
        wf.quest = wf.explore(dam.quest, notes, me)
    elif position == 42: # Rathaus
        townhall.explore(me)
    else:
        print("You're out of map lul")

def printposition(position): #TODO mach match-case draus
    if position == 11:
        print("--Wald--")
    elif position == 12:
        print("--Wald--")
    elif position == 13:
        print("--Wald--")
    elif position == 22:
        print("--Wald--")
    elif position == 23:
        print("--Staudamm--")
    elif position == 30:
        print("--Vogelhaus--")
    elif position == 31:
        print("--Aquarium--")
    elif position == 32:
        print("--Dorfplatz--")
    elif position == 33:
        print("--Wasserfall--")
    elif position == 42:
        print("--Rathaus--")
    else:
        print("You're out of map lul")


# quest can be: open; active; done; 
map.printMap()
notes.read()

#TODO Stelle sicher, dass es verschiedene Arten von Angriffen gibt, die der Spieler verwenden kann, z.B. physische -, oder magische Angriffe
# oder Statusveränderungen. Jeder Angriffstyp sollte seine eigenen Vor- und Nachteile haben, so dass der Spieler strategisch vorgehen muss.
#TODO Zeit abbrechen wenn alle fragen durch sind
#TODO maybe bei nicht bestandenem quiz, hinweis in die notes schreiben?

block = False # avoids two fights after another
while me.lives > 0:
    print("Was möchtest du machen?")
    doing = input(">")
    if doing == "umschauen":
        fight = random.choices((True, False), weights = [1, 3])
        if fight[0] and not block:
           villain = random.choice(villains)
           villain.printInfo()
           me.fight(villain)
           block = not block
        else:       
            checkaction(me.positionNow)
            block = not block
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