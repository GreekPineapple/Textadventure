from enemy import *
from map import *
chef = Enemy(100,10)
villager = Enemy(50, 10)
me = Player(55, 10, ["eins", "zwei"], 42)
townhall = TownHall()

#townhall.start()
#print(me.inventory)
#chef.fight(me)


#villager.fight(me)


while 1 > 0:
    me.move()
    #fight(mylives)
 #  me.move(v, h)