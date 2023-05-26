import random, time
from person import Player, Villain
from map import *
from notes import *
map = Map(4,4)
me = Player(200, 10, "myself", ["eins", "zwei"], 42) #Start: Townhall
townhall = TownHall()
woods = Woods("open")
wf = Waterfall("open")
dam = Dam("open")
aquarium = Aquarium("open")
square = Square()
birdhouse = BirdHouse("open")
notes = Notes()
villain1 = Villain(80, 10, "villain1", 8, 7, 6, 5, 4, 11)
villain2 = Villain(100, 20, "villain2", 18, 17, 16, 15, 4, 11)

villains = [villain1, villain2]

def checkposition(position): #TODO mach match-case draus
    if position == 11:
        print("--Wald--")
    elif position == 12:
        print("--Wald--")
    elif position == 13:
        print("--Wald--")
    elif position == 22:
        print("--Wald--")
        woods.quest = woods.explore(birdhouse.quest, notes)
    elif position == 23:
        print("--Staudamm--")
        dam.quest = dam.explore(wf.quest, aquarium.quest, me, notes)
    elif position == 30:
        print("--Vogelhaus--")
        birdhouse.quest = birdhouse.explore(aquarium.quest, woods.quest, notes)
    elif position == 31:
        print("--Aquarium--")
        aquarium.quest = aquarium.explore(dam.quest, birdhouse.quest, me, notes)
    elif position == 32:
        print("--Dorfplatz--")
    elif position == 33:
        print("--Wasserfall--")
        wf.quest = wf.explore(dam.quest, notes)
    elif position == 42:
        print("--Rathaus--")
        townhall.explore()
    else:
        print("You're out of map lul")

#me.fight(villain1)
# quest can be: open; active; done; 
map.printMap()
notes.read()

#TODO Stelle sicher, dass es verschiedene Arten von Angriffen gibt, die der Spieler verwenden kann, z.B. physische -, oder magische Angriffe
# oder Statusveränderungen. Jeder Angriffstyp sollte seine eigenen Vor- und Nachteile haben, so dass der Spieler strategisch vorgehen muss.
#TODO ein array mit antwortmöglichkeiten [yes, y, ja, j, jop, jap, jep] und bei jeder frage nur ein if antwort in array
#TODO nach dem laufen anzeigen wo man steht

while me.lives > 0:
    print("Was möchtest du machen?")
    doing = input(">")
    if doing == "umschauen":
        fight = bool(random.getrandbits(1))
        if fight:
            villain = random.choice(villains)
            me.fight(villain)
        else:       
            checkposition(me.positionNow)
    elif doing == "laufen":
        me.move(wf.quest)
    elif doing == "help":
        notes.read()
    elif doing == "map":
        map.printMap()
    elif doing == "ende":
        break
    else:
        print("ungültige eingabe")
print("GAME OVER!")