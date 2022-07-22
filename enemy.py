class Enemy:
    def __init__(self, lives, strength):
        self.lives = lives
        self.strength = strength
        
    def printInfo (self):
        print("Leben: " + str(self.lives) )
        print("Stärke: " + str(self.strength) )

    def fight(self, player):
        print("Oh nein, du wirst angegriffen! :(")
        while self.lives > 0:
            print("Du kannst\na) Angreifen\nb) Verteidigen\nc) Trank nehmen")
            option = input(">")
            if option.lower() == "a":
                self.lives -= player.strength
                print("Du hast angegriffen, der gegner hat noch " + str(self.lives) + " Leben")
            elif option.lower() == "b":
                print("Du bist dem Gegner ausgewichen und verlierst keine Leben")
            elif option.lower() == "c":
                print("Du hast folgende Tränke zur verfügung: " + str(player.inventory))
                potion = input("Welchen Trank möchtest du nutzen?")
                if potion in player.inventory:
                    print("jupii")
                else: 
                    print("not in you inventory")
            player.lives -= self.strength
            print("Der Gegner greift an, du hast noch " + str(player.lives) + " Leben")

class Player(Enemy):
    def __init__(self, lives, strength, inventory, positionNow):
        self.inventory = inventory
        self.positionNow = positionNow
        super().__init__(lives, strength)

    def move(self): #laufen möglich, geheimwege fehlen noch
        a = [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]]
        #for i in range(len(a)):
         #   for j in range(len(a[i])):
          #      print(a[i][j], end=' ')
           # print()
        position = self.positionNow
        
        print("In welche Richtung möchtest du gehen? (N/O/S/W)")
        direction = input(">")
        if direction.lower() == "n":
            if position == 30:
                print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
            elif position == 33:
                print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")                    
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
            if position == 23:
                print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")                
            elif position == 11 or position == 13 or position == 30 or position == 31 or position == 33 or position == 42:
                print("Hier gibt es keinen weg nach Sueden")
            else:
                print("Du gehst nach Sueden")
                position += 10
        elif direction.lower() == "w":
            if position == 22:
                print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
            elif position == 11 or position == 23 or position == 30 or position == 42:
                print("Hier gibt es keinen weg nach Westen")
            else:
                print("Du gehst nach Westen")
                position -= 1
        else:
            print("Ungültige Eingabe")
        self.positionNow = position
        