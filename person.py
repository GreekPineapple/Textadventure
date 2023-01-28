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
    def __init__(self, lives, strength, name, red, yellow, blue, purple, orange, defence):
        self.red = red
        self.yellow = yellow
        self.blue = blue
        self.purple = purple
        self.orange = orange
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
        for i in range(len(a)):
            for j in range(len(a[i])):
                print(a[i][j], end=' ')
            print()
        position = self.positionNow
        
        print("In welche Richtung möchtest du gehen? (N/O/S/W)")
        direction = input(">")

        if direction.lower() == "n":
            if position == 30:
                print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
            elif position == 33 and wfquest == "done":
                print("Diesen Weg gibt es leider nichtmehr. Hier fließt jetzt Wasser!")                               
            elif position == 11 or position == 12 or position == 13 or position == 23 or position == 31:
                print("Hier gibt es keinen weg nach Norden")
            else:
                print("Du gehst nach Norden")
                position -= 10

        elif direction.lower() == "o":
            if position == 13 or position == 23 or position == 33 or position == 42:
                print("Hier gibt es keinen weg nach Osten")
            else:
                print("Du gehst nach Osten")
                position += 1
        
        elif direction.lower() == "s":
            if position == 23 and wfquest == "done" :
                print("Diesen Weg gibt es leider nichtmehr. Hier fließt jetzt Wasser!")               
            elif position == 11 or position == 13 or position == 30 or position == 31 or position == 33 or position == 42:
                print("Hier gibt es keinen weg nach Sueden")
            else:
                print("Du gehst nach Sueden")
                position += 10
        
        elif direction.lower() == "w":
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
        specialAttack = False
        #first: shopping!
        tempinventory = []
        defencepoints = 1
        shop = {"red": 5, "yellow": 4, "blue": 3, "purple": 2, "orange": 1, "defence": 10} #key -> item, value -> price
        print("Du wirst angegriffen :( Kaufe deine Ausrüstung im Shop:")
        print("Roter Angriff (-5 Leben)  Gelber Angriff (-4 Leben)  Blauer Angriff (-3 Leben)  Lila Angriff (-2 Leben)  Orangener Angriff (-1 Leben)  Verbesserte Verteidigung (-10 Leben)")
        item = input(">")
        while item != "ende":
            if item in shop:
                self.lives -= shop[item]
                tempinventory.append(item)
                print("Du hast noch: " + str(self.lives) + " leben")
            else:
                print("Diesen Artikel haben wir nicht im Angebot")
            item = input(">")
        print("Dein Inventar für den Kampf: " + str(tempinventory)) #TODO Defence begrenzen! Sonst macht Gegner irgendwann keinen schaden mehr
      
        while self.lives > 0 and villain.lives > 0:
            print(self.lives > 0)
            print(villain.lives > 0)
            use = input("Wie möchtest du angreifen?")
            specialAttack = False
            if use == "red" and use in tempinventory:
                villain.lives -= villain.red
                tempinventory.remove("red")
                if villain.name == "villain1":
                    specialAttack = True
            elif use == "yellow" and use in tempinventory:
                villain.lives -= villain.yellow
                tempinventory.remove("yellow")
            elif use == "blue" and use in tempinventory:
                villain.lives -= villain.blue
                tempinventory.remove("blue")
            elif use == "purple" and use in tempinventory:
                villain.lives -= villain.purple
                tempinventory.remove("purple")
            elif use == "orange" and use in tempinventory:
                villain.lives -= villain.orange
                tempinventory.remove("orange")
            elif use == "defence" and use in tempinventory:
                defencepoints -= 0.1
                tempinventory.remove("defence")
            else:
                print(use + " ist nicht in deinem Inventar, bitte wähle eine andere option aus!")
            print("Dein Inventar: " + str(tempinventory))
            print("Gegner Leben nach dem Angriff: " + str(villain.lives))
            print("Du wirst angegriffen")
            if specialAttack:
                print("Deine Angriffsattacke hat den gegner wohl wütend gemacht, er greift stärker an :0")
                self.lives -= villain.strength * defencepoints + 20
                print("Deine Leben danach: " + str(self.lives))
            else:
                self.lives -= villain.strength * defencepoints
                print("Deine Leben danach: " + str(self.lives))
            if self.lives <= 0:
                print("Du bist rip")
            elif villain.lives <= 0:
                print("Der Gegener ist rip")