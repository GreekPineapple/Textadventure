import random
class Person:
    def __init__(self, lives, strength, name):
        self.lives = lives
        self.strength = strength
        self.name = name
        
    def printInfo (self):
        print("Leben: " + str(self.lives) )
        print("Stärke: " + str(self.strength) )
        print("Name: " + str(self.name) )

class Villain (Person):
    def __init__(self, lives, strength, name, red, yellow, blue, purple, kick, defence):
        self.red = red
        self.yellow = yellow
        self.blue = blue
        self.purple = purple
        self.kick = kick
        self.defence = defence
        super().__init__(lives, strength, name)

    def printInfo(self):
        return super().printInfo()

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
        redcount = yellowcount = bluecount = purplecount = 0
        #first: shopping!
        inventory = ["kick"]
        defencepoints = 1
        shop = {"red": 5, "yellow": 4, "blue": 3, "purple": 2, "defence": 10, "healing": 7} #key -> item, value -> price
        print('Du wirst angegriffen :( Kaufe deine Ausrüstung im Shop (beende deinen Einkauf mit "ende"):')
        print("Roter Angriff (-5 Leben)  Gelber Angriff (-4 Leben)  Blauer Angriff (-3 Leben)  Lila Angriff (-2 Leben)  Verbesserte Verteidigung (-10 Leben), Heilung (-7 Leben)")
        item = input(">")
        while item != "ende": #TODO Do while schleife?
            if item.lower().strip() in shop:
                self.lives -= shop[item]
                inventory.append(item.strip())
                print("Du hast noch: " + str(self.lives) + " leben")
            else:
                print("Diesen Artikel haben wir nicht im Angebot")
            item = input(">")
        print("Dein Inventar für den Kampf: " + str(inventory)) #TODO Defence begrenzen! Sonst macht Gegner irgendwann keinen schaden mehr
      
        while self.lives > 0 or villain.lives > 0:
            print('Wie möchtest du angreifen? Du kannst 2 Angriffe auswählen um Kombo boni zu erhlaten, musst aber nicht. (Tippe "none" wenn du nur einen Angriff machen willst)')
            #choose 1 or 2 attacks:
            use = input("1. Angriff: ")
            while use not in inventory or use == "healing":
                print("ungültig")
                use = input("1. Angriff: ")
            bonus = input("2. Angriff: ")
            while bonus != "none" and bonus not in inventory or bonus == "healing":
                print("ungültig")
                bonus = input("2. Angriff: ")
            round = [use, bonus]
            #attack:
            if "red" in round:
                if redcount > 3:
                    print("Rot macht keinen Schaden mehr")
                else:
                    print("red wurde benutzt")
                    inventory.remove("red")
                    if bonus == "red" and  use == "red":
                        print("Red wurde nochmal benutzt")
                        inventory.remove("red")
                        villain.lives -= villain.red + 10
                    redcount+=1
                    villain.lives -= villain.red
            if "yellow" in round:
                if yellowcount > 3:
                    print("Yellow macht keinen Schaden mehr")
                else:
                    print("yellow wurde benutzt")
                    if bonus == "yellow" and use == "yellow":
                        print("Gelb wurde nochmal benutzt")
                        villain.lives -= villain.yellow + 10
                    villain.lives -= villain.yellow
                    inventory.remove("yellow")
                    yellowcount += 1
            if "blue" in round:
                if bluecount > 3:
                    print("Blue macht keinen Schaden mehr")
                else:
                    print("blau wurde benutzt")
                    if bonus == "blue" and use == "blue":
                        print("blau wurde nochmal benutzt")
                        villain.lives -= villain.blue + 10
                    villain.lives -= villain.blue
                    inventory.remove("blue")
                    bluecount += 1
            if "purple" in round:
                if purplecount > 3:
                    print("Purple macht keinen Schaden mehr")
                else:
                    print("lila wurde benutzt")
                    if bonus == "purple" and use == "purple":
                        print("lila wurde nochmal benutzt")
                        villain.lives -= villain.purple + 10
                    villain.lives -= villain.purple
                    inventory.remove("purple")
                    purplecount += 1
            if "kick" in round: #always possible
                villain.lives -= villain.kick
            if "defence" in round:
                defencepoints -= 0.1
                inventory.remove("defence")
            print("Dein Inventar: " + str(inventory))
            print("Gegner Leben nach dem Angriff: " + str(villain.lives))
            if redcount > 3 or yellowcount > 3:
                print("\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n")

            print("Du wirst angegriffen")
            special_attack = random.random()
            if special_attack < 0.25: #probabilty of 25% that enemy makes a special attack
                print("Der gegner hat dich eingefroren, so kannst du nicht kämpfen.")
                if "healing" in inventory:
                    print("Möchtest du deinen Heiltrank nutzen? (y/n)")
                    healing = input(">")
                    if healing == "ja" or healing == "j" or healing == "yes" or healing == "y":
                        inventory.remove("healing")
                    else:
                        print("Du wirst angegriffen")
                        self.lives -= villain.strength * defencepoints
                else:
                    print("Du wirst angegriffen")
                    self.lives -= villain.strength * defencepoints
            else:
                self.lives -= villain.strength * defencepoints
                print("Deine Leben danach: " + str(self.lives))
            if self.lives <= 0:
                print("Du bist rip")
            elif villain.lives <= 0:
                print("Der Gegener ist rip")