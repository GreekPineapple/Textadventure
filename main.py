import random
from enemy import *
from map import *
chef = Enemy(100,10)
villager = Enemy(50, 10)
me = Player(55, 10, ["eins", "zwei"], 42)
townhall = TownHall()

#townhall.start()

i = 8
while i > 5:
    print ("Was mächtest du machen?")
    doing = input(">")
    if doing == "umschauen":
        fight = random.randint(1,2)
        if fight == 1:
            villager.fight(me)
        else:
            if me.positionNow == 42:
                townhall.explore()
   
        print(me.positionNow)
    elif doing == "laufen":
        me.move()
    else:
        print("ungültige eingabe")