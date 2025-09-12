import random, json, globals
from collections import Counter
from inventory import Inventory
from person import Person
from trivia import *
import shop as shop

class Player(Person):
    
    secretPath = False
    
    def __init__(self, lives, strength, name, armmor_points, inventory, positionNow):
        self.armmor_points = armmor_points
        self.inventory = Inventory(inventory)
        self.positionNow = positionNow
        super().__init__(lives, strength, name)

    def printInfo(self):
        return super().printInfo()

    def move(self, wfquest):
        a = [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]]
        # for i in range(len(a)):
        #     for j in range(len(a[i])):
        #         print(a[i][j], end=" ")
        #     print()
        position = self.positionNow
        
        print(f"In welche Richtung möchtest du gehen? ({globals.COLOR_COMMAND}N/O/S/W{globals.COLOR_RESET})")
        direction = input(f"{globals.COLOR_INPUT}>").lower().strip()
        print(f"{globals.COLOR_RESET}")
        if direction == "n":
            if position == 30:
                if not self.secretPath:
                    print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
                    answer = input(f"Möchtest du jetzt dein Wissen unter Beweis stellen? ({globals.COLOR_COMMAND}ja/nein{globals.COLOR_RESET})").lower().strip()
                    if answer == "ja":
                        if Trivia.main(Trivia, self):
                            position = 22
                else:
                    print("Du gehst den Geheimweg")
                    position = 22
            elif position == 33 and wfquest == "done":
                print("Diesen Weg gibt es leider nichtmehr. Hier fließt jetzt Wasser!")                               
            elif position in {11, 12, 13, 23, 31}:
                print("Hier gibt es keinen weg nach Norden")
            else:
                print("Du gehst nach Norden")
                position -= 10

        elif direction == "o":
            if position in {13, 23, 33, 42}:
                print("Hier gibt es keinen weg nach Osten")
            else:
                print("Du gehst nach Osten")
                position += 1
        
        elif direction == "s":
            if position == 23 and wfquest == "done" :
                print("Diesen Weg gibt es leider nichtmehr. Hier fließt jetzt Wasser!")               
            elif position in { 11, 13, 30, 31, 33, 42}:
                print("Hier gibt es keinen weg nach Sueden")
            else:
                print("Du gehst nach Sueden")
                position += 10
        
        elif direction == "w":
            if position == 22:
                if not self.secretPath:
                    print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
                    answer = input(f"Möchtest du jetzt dein Wissen unter Beweis stellen? ({globals.COLOR_COMMAND}ja/nein{globals.COLOR_RESET})").lower().strip()
                    if answer == "ja":
                        if Trivia.main(Trivia, self):
                            position = 30
                else:
                    print("Du gehst den Geheimweg")
                    position = 30
            elif position in {11, 30, 42}:
                print("Hier gibt es keinen weg nach Westen")
            else:
                print("Du gehst nach Westen")
                position -= 1
        else:
            print("Ungültige Eingabe")
        self.positionNow = position

    def fight(self, villain, angriffe): 
        tempLives = self.lives
        temp_strength = self.strength
        fightInventory = ["kick"]

        shop.shop(self, fightInventory, angriffe)
        vc = Inventory(Counter(fightInventory))
       
        while self.lives > 0 or villain.lives > 0:

            # --- Player attack --- #
          
            print(str(vc).replace("Counter", f"Dein {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} für den Kampf: "))
            round, vc = shop.choose(vc)
            strength_bonus = 1

            damage = 0
            for angriff in angriffe:
                if angriff.type.lower().strip() == "defence":
                    value = 0.2 if round[0] == round[1] else 0.1
                    self.armmor_points -= value
                elif round[0] == round[1]:
                    print("Solch einen speziellen Angriff zu machen, raubt dir deine Kraft, du verlierst 10 Leben")
                    strength_bonus = 2.5
                    self.lives -= 10
                elif angriff.name.lower().strip() in round and angriff.make_damage(villain) > 0:
                    damage += angriff.make_damage(villain)                  
                
            if "kick" in round:
                damage += self.strength
            
            villain.lives -= damage * strength_bonus
    
            print(f"Der Gegner hat noch {villain.lives} Leben übrig\n")
            
            # --- Villain attack --- #

            self.strength = temp_strength
            for effect in villain.active_effects:
                effect.use_effect(villain)

            if not villain.blocked:
                villain.attack(self)
            else:
                print("Der Gegner wurde vergiftet und kann nicht angreifen")
        
            if self.lives <= 0:
                print("Du wurdest besiegt und verlierst 10 Leben")
                self.lives = tempLives - 10
                break
            elif villain.lives <= 0:
                drop = "Gutschein" if random.random() < 0.20 else villain.drop
                print(f"Glückwunsch, du hast den Gegner besiegt, zur belohnung bekommst du: {drop}")
                self.inventory[drop] += 1
                self.lives = tempLives
                break
