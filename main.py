import random, time
from person import Player, Villain
from map import *
from notes import *
map = Map(4,4)
me = Player(200, 10, "myself", ["eins", "golem überreste", "Heiltrank", "vogel überreste", "bombe", "Gutschein", "goblin überreste", "goblin überreste", "bombe", "wizard überreste"], 42) #Start: Townhall
townhall = TownHall()
woods = Woods("open")
wf = Waterfall("open")
dam = Dam("open")
aquarium = Aquarium("open")
square = Square()
birdhouse = BirdHouse("open")
notes = Notes()

#the smaller the resistance, the smaller the damage (Muss vielleicht *-1 machen, damit sprachlich sinn ergibt xD)
goblin = Villain("Goblin", 40, 100, 1, [5, 0, 10], "goblin überreste")
golem = Villain("Erdgolem", 100, 40, 4, [20, 15, 10], "golem überreste")
wizard = Villain("Magier", 80, 80, 6, [5, 10, 15], "wizard überreste")
luftGegner = Villain("Luftgegner", 60, 50, 2, [5, 20, 0], "vogel überreste")

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

#townhall.explore(me)
me.boss(villains)
#me.fight(golem)
# quest can be: open; active; done; 
#map.printMap()
#notes.read()

#TODO Stelle sicher, dass es verschiedene Arten von Angriffen gibt, die der Spieler verwenden kann, z.B. physische -, oder magische Angriffe
# oder Statusveränderungen. Jeder Angriffstyp sollte seine eigenen Vor- und Nachteile haben, so dass der Spieler strategisch vorgehen muss.
#TODO Zeit abbrechen wenn alle fragen durch sind
#TODO maybe bei nicht bestandenem quiz, hinweis in die notes schreiben?
#TODO Shop mit json machen

# Für den Bosskampf gibt es keinen shop, man verwendet dinge die von einem normalen gegner gedroppt werden, nachdem man diesen besiegt. Man braucht aber spezial angriffe von jedem gegner dens gibt um den boss zu besiegen
# Wenn man einen kampf mit dem normalen gegner verliert, verliert man auch ein leben. mit diesen leben (schon implementiert) geht man dann in den bosskampf. (außer man hat heilung)

# Gegner droppen gutscheine oder deren üverreste also z.b. magier droppt mageier überreste, goblin droppt goblin überreste
# gutscheine um ausrüstung und heilung zu kaufen

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