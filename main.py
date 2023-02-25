import random, time
from person import Player, Villain
from map import *
from notes import *
me = Player(200, 10, "myself", ["eins", "zwei"], 42) #Start: Townhall
townhall = TownHall()
woods = Woods("open")
wf = Waterfall("open")
dam = Dam("open")
aquarium = Aquarium("open")
square = Square()
birdhouse = BirdHouse("open")
notes = Notes()
villain1 = Villain(101, 10, "villain1", 8, 7, 6, 5, 4, 11)
villain2 = Villain(100, 20, "villain2", 20, 7, 6, 5, 4, 11)

villains = [villain1, villain2]

def checkposition(position):
    if position == 11:
        pass #woods
    elif position == 12:
        pass # woods
    elif position == 13:
        pass # woods
    elif position == 22:
        woods.quest = woods.explore(birdhouse.quest, notes)
        print("woods.wuest nach explore: " + woods.quest)
    elif position == 23:
        dam.quest = dam.explore(wf.quest, aquarium.quest, me, notes)
    elif position == 30:
        birdhouse.quest = birdhouse.explore(aquarium.quest, woods.quest, notes)
    elif position == 31:
        aquarium.quest = aquarium.explore(dam.quest, birdhouse.quest, me, notes)
    elif position == 32:
        pass # Dorfplatz
    elif position == 33:
        wf.quest = wf.explore(dam.quest, notes)
    elif position == 42:
        townhall.explore()
    else:
        print("You're out of map lul")

# quest can be: open; active; done; 

#me.fight(villain1)
#notes.countdown()
while me.lives > 0:
    print("Was möchtest du machen?")
    doing = input(">")
    if doing == "umschauen":
        fight = bool(random.getrandbits(1))
        print(fight)
        if fight:
            villain = random.choice(villains)
            me.fight(villain)
        else:       
            checkposition(me.positionNow)
    elif doing == "laufen":
        me.move(wf.quest)
    elif doing == "ende":
        break
    else:
        print("ungültige eingabe")
print("GAME OVER!")