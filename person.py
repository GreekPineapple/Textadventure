positiveAnswers = ["yes", "y", "ja", "j", "yep", "jop"]
import random
from collections import Counter

class Person:
    def __init__(self, lives, strength, name):
        self.lives = lives
        self.strength = strength
        self.name = name
        
    def printInfo (self):
        print("Name: " + str(self.name) )
        print("Leben: " + str(self.lives) )
        print("Stärke: " + str(self.strength) )

class Villain (Person):
    def __init__(self, lives, strength, name, defence):
        self.water = lives / 100 * 5
        self.arrow = lives / 100 * 15
        self.sword = lives / 100 * 10
        if name == "Goblin":
            self.arrow = lives / 100 * 0 #goblin is too fast
        elif name == "Erdgolem":
            self.water = lives / 100 * 20
        elif name == "Luftgegner":
            self.sword = lives / 100 * 0 #logisch i guess
            self.arrow = lives / 100 * 20

        self.kick = lives / 100 * 4
        self.defence = defence
        super().__init__(lives, strength, name)

    def printInfo(self):
        super().printInfo()
        print("Eigenschaften: " + str(self.strength) )

class Player(Person):
    def __init__(self, lives, strength, name, inventory, positionNow):
        self.inventory = inventory
        self.positionNow = positionNow
        super().__init__(lives, strength, name)

    def printInfo(self):
        return super().printInfo()

    def move(self, wfquest): #laufen möglich, geheimwege fehlen noch
        a = [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]]
        # for i in range(len(a)):
        #     for j in range(len(a[i])):
        #         print(a[i][j], end=" ")
        #     print()
        position = self.positionNow
        
        print("In welche Richtung möchtest du gehen? (N/O/S/W)")
        direction = input(">")
        if direction.lower().strip() == "n":
            if position == 30:
                print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
            elif position == 33 and wfquest == "done":
                print("Diesen Weg gibt es leider nichtmehr. Hier fließt jetzt Wasser!")                               
            elif position == 11 or position == 12 or position == 13 or position == 23 or position == 31:
                print("Hier gibt es keinen weg nach Norden")
            else:
                print("Du gehst nach Norden")
                position -= 10

        elif direction.lower().strip() == "o":
            if position == 13 or position == 23 or position == 33 or position == 42:
                print("Hier gibt es keinen weg nach Osten")
            else:
                print("Du gehst nach Osten")
                position += 1
        
        elif direction.lower().strip() == "s":
            if position == 23 and wfquest == "done" :
                print("Diesen Weg gibt es leider nichtmehr. Hier fließt jetzt Wasser!")               
            elif position == 11 or position == 13 or position == 30 or position == 31 or position == 33 or position == 42:
                print("Hier gibt es keinen weg nach Sueden")
            else:
                print("Du gehst nach Sueden")
                position += 10
        
        elif direction.lower().strip() == "w":
            if position == 22:
                print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
            elif position == 11 or position == 30 or position == 42:
                print("Hier gibt es keinen weg nach Westen")
            else:
                print("Du gehst nach Westen")
                position -= 1
        else:
            print("Ungültige Eingabe")
        self.positionNow = position

    def fight(self, villain): 
        watercount = arrowcount = swordcount = 0
        inventory = ["kick"]
        defencepoints = 1
        specialAttacks = ["jump", "heat"]
        self.shop_normal(inventory)
        vc = Counter(inventory)
        value_counts_str = str(vc).replace("Counter", "Dein Inventar für den Kampf: ")
       
        while self.lives > 0 or villain.lives > 0:
            vc = +vc #without 0's
            print(vc)
            print('Wie möchtest du angreifen? Du kannst 2 Angriffe auswählen um Kombo boni zu erhlaten, musst aber nicht. (Tippe "none" wenn du nur einen Angriff machen willst)')
            #choose 1 or 2 attacks:

            use = input("1. Angriff: ")
            while use.lower().strip() not in vc or use.lower().strip() in specialAttacks:
                print("ungültig")
                use = input("1. Angriff: ")
            use = use.lower().strip()
            if not use == "kick":
                vc[use] -= 1
            vcs = str(vc).replace("Counter", "after one eingabe: ")
            print(vcs)
            vc = +vc

            bonus = input("2. Angriff: ")
            while bonus.lower().strip() != "none" and bonus.lower().strip() not in vc or bonus.lower().strip() in specialAttacks:
                print("ungültig")
                bonus = input("2. Angriff: ")
            bonus = bonus.lower().strip()
            if not bonus == "kick":
                vc[bonus] -= 1
            vcs2 = str(vc).replace("Counter", "after two eingabe: ")
            print(vcs2)

            round = [use, bonus]
            if "water" in round:
                if watercount > 3:
                    print("water macht keinen Schaden mehr")
                else:
                    print("water wurde benutzt")
                    if bonus == "water" and  use == "water":
                        print("water wurde nochmal benutzt")
                        villain.lives -= villain.water * 1.5
                        watercount+=1
                    villain.lives -= villain.water
                    watercount+=1
            if "arrow" in round:
                if arrowcount > 3:
                    print("arrow macht keinen Schaden mehr")
                else:
                    print("arrow wurde benutzt")
                    if bonus == "arrow" and use == "arrow":
                        print("arrow wurde nochmal benutzt")
                        villain.lives -= villain.arrow * 1.5
                        arrowcount += 1
                    villain.lives -= villain.arrow
                    arrowcount += 1
            if "sword" in round:
                if swordcount > 3:
                    print("sword macht keinen Schaden mehr")
                else:
                    print("sword wurde benutzt")
                    if bonus == "sword" and use == "sword":
                        print("sword wurde nochmal benutzt")
                        villain.lives -= villain.sword * 1.5
                        swordcount += 1
                    villain.lives -= villain.sword
                    swordcount += 1
            if "kick" in round: #always possible
                villain.lives -= villain.kick
            if "defence" in round:
                defencepoints -= 0.1
            print("Gegner Leben nach dem Angriff: " + str(villain.lives))
            if watercount > 3 or arrowcount > 3 or swordcount > 3:
                print("\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n")

            print("Du wirst angegriffen")
            special_attack = random.random()
            if special_attack < 0.25: #probabilty of 25% that enemy makes a special attack
                print("Der gegner macht einen spezialangriff")
                if villain.name == "Erdgolem" and "jump" in vc:
                    print("du weichst dem spezialangruff des golems aus")
                    vc["jump"] -= 1
                elif villain.name == "Magier" and "heat" in vc:
                    print("der Magier hat dich eingefroren, aber du taust dich wieder auf")
                    vc["heat"] -= 1
                else:
                    print("Du wirst mit spezialattacke angegriffen")
                    self.lives -= villain.strength * 2 * defencepoints
            else:
                self.lives -= villain.strength * defencepoints
                print("Deine Leben danach: " + str(self.lives))
            if self.lives <= 0:
                print("Du bist rip")
                break
            elif villain.lives <= 0:
                print("Der Gegener ist rip")
                break
    
    def shop_normal(self,inventory):
        defenceCount = 0

        #TODO für den pfeil noch 1 Bogen kaufen?; details zu den angriffen anzeigen?

        shop = {"water": 2, "arrow": 4, "sword": 3, "defence": 8, "jump": 10, "heat": 10} #key -> item, value -> price
        print('Du wirst angegriffen :( Kaufe deine Ausrüstung im Shop (beende deinen Einkauf mit "ende"):')
        print("\u001b[4mAngriffe:\u001b[0m \nWater (-2 Leben); Arrow (-4 Leben); Sword (-3 Leben)")
        print("\u001b[4mAusweichmanöver:\u001b[0m \njump (-10 Leben); heat (-10 Leben)")
        print("\u001b[4mVerteidigungen:\u001b[0m \nEigene defence (-8 Leben)")
        item = input(">")
        while item.lower().strip() != "ende": #TODO Do while schleife?
            if item.lower().strip() == "defence":
                defenceCount += 1
            if item.lower().strip() in shop:
                if defenceCount <= 5:
                    self.lives -= shop[item.lower().strip()]
                    inventory.append(item.lower().strip())
                    print("Du hast noch: " + str(self.lives) + " leben")
                else:
                    print("Du darfst nur 5 mal deine Verteidugng verbessern, wähle was anderes aus.")
            else:
                print("Diesen Artikel haben wir nicht im Angebot")
            item = input(">")

    
    def shop_boss(self,inventory):
        pass