from collections import Counter
import json, random
import globals, shop
from inventory import Inventory

class Boss:

    def __init__(self):
        self.lives = 200
        self.strength = 80
        self.name = "Boss"
        self.dot_damage = 5

    def printInfo (self):
        print(f"\nDu wirst vom {globals.COLOR_NOUN}{self.name}{globals.COLOR_RESET} angegriffen")
        print(f"Leben: {self.lives}")
        print(f"Stärke: {self.strength}\n" )

    def fight(self, villains, player):
        protection = 0
        remainingLayers = len(villains)
        print(f"Für den {globals.COLOR_NOUN}Bosskampf{globals.COLOR_RESET} nutzt du die Angriffe aus deinem {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} und deine tatsächlichen Leben")

        possibleItems = []
        items = self.filterJsonBoss()
        for item in items:
            possibleItems.append(item["name"])

        protectiveLayer = []
        for villain in villains:
            protectiveLayer.append(villain.drop)

        combinedList = set(possibleItems) | set(protectiveLayer)
        inventory = Inventory(Counter({key: player.inventory.get_item(key) for key in combinedList}))
        inventory.print_inventory()

        # --- Phase 1 --- #
        while remainingLayers > 0:
            print(f"Der Gegner hat ein {globals.COLOR_NOUN}Schutzschild{globals.COLOR_RESET} um sich herum, welches nur mit den {globals.COLOR_NOUN}überresten{globals.COLOR_RESET} der besiegten gener zerstört werden kann. Insgesammt gibt es noch {remainingLayers} Schutzschichten. Du kannst nicht zwei schichten mit den gleichen überresten zerstören, und immer nur eine schicht gleichzeitig pro angriff zerstören.\n")
            
            round = shop.choose(inventory)
            attacks = round[0]

            if attacks[0] in protectiveLayer and attacks[1] in protectiveLayer and attacks[0] != attacks[1]:
                print(f"die überreste vermischen sich und wirken nicht gegen das {globals.COLOR_NOUN}Schutzschild{globals.COLOR_RESET}, hättest du mal zugehört ")

            elif not attacks[0] in protectiveLayer and not attacks[1] in protectiveLayer:
                print("Der Gegner hat eine schutzschicht")
            
            elif any(element in attacks for element in protectiveLayer) or attacks[0] == attacks[1]:
                if attacks[1] != "none" and attacks[0] != attacks[1]:
                    print("Deine normale attacke ist leider nutzlos")
                remainingLayers -=1
                protectiveLayer[:] = [element for element in protectiveLayer if element not in attacks]

                print(f"\nSuper, du hast eine schicht entfernt, es fehlen noch {protectiveLayer}")
            
        print(f"Du hast die {globals.COLOR_NOUN}Schutzschicht{globals.COLOR_RESET} des gegners gebrochen, jetzt kannst du angreifen")

        # --- Phase 2 --- #

        dot_rounds = 0
        healing_block = False
        bomb_count = 3
        while player.lives > 0 or self.lives > 0:

            # --- Player attack --- #
            round, inventory = shop.choose(inventory)
          #  attacks = round[0]
            items = self.filterJsonBoss()
            paralize = False
            for attack in round:
                print(attack)
                if attack in [item["name"] for item in items]:
                    print(item["name"], "ist der name")
                    if item["name"] == "heiltrank":
                        if not healing_block:
                            player.lives = 250
                            healing_block = True
                        else:
                            print("Du kannst den heiltrank nur einmal im kampf nutzen")
                    if item["name"] == "laehmungstrank":
                        paralize = True
                    if item["type"] == "Schutz":
                        protection += 10
                    if item["name"] == "bombe":
                        if bomb_count > 0:
                            bomb_count -= 1
                        else:
                            print("Du hast keine Bomben mehr")
                    print(item["name"])
                    self.lives -= item["damage"]

            print(f"\nGegner Leben: {self.lives} \n Deine Leben: {player.lives}\n")

            if self.lives <= 0:
                print("Glückwunsch, Gegner ist tot, hier ist das letzte fehlende Bauteil")
                player.inventory["Bauteil3"] += 1
                break
            
            # --- Villain attack --- #

            if self.lives <= 90 and dot_rounds == 0:
                dot_rounds = 3
                print("Der Boss hat die hälfte seiner leben verloren, er ist wütend und vergiftet dich. :(")

            if dot_rounds > 0:
                player.lives -= self.dot_damage
                dot_rounds -= 1
                print(f"Du bist vergiftet! -{self.dot_damage} Leben.")

            if paralize:
                print("Der Gegner ist gelähmt und kann dich für eine Runde nicht angreifen")
                paralize = False
            else:
                print("Du wirst angegriffen")
                specialAttack = random.random()
                if specialAttack < 0.25: #probabilty of 25% that enemy makes a special attack
                    print("Der gegner nutzt die Energie der Toten Gegner um einen Spezial angruff zu machen. Wehre ihn entweder mit den passenden Überresten ab, oder nutze den Lehmungstrank in der nächsten Runde.")
                    print("Hast du nichts von beiden, bekommst du doppelten Schaden.")
                    round = shop.choose(inventory)
                    attacks = round[0]
                    if any(element in attacks for element in protectiveLayer) or "laehmungstrank" in attacks[0]:
                        print("yaay Du whrst den schaden ab")
                    else:
                        print("Der Gegner trifft dch mit mehr schaden :((")
                        player.lives -= (self.strength - protection) * 1.5 

                else:
                    player.lives -= self.strength  - protection

                if player.lives <= 0:
                    print("Du wurdest besiegt. Den nächstem Kampf bestreitest du mit 10 Leben weniger.")
                    player.lives = 240
                    break

                print(f"\nGegner Leben: {self.lives} \n Deine Leben: {player.lives}\n")

    def filterJsonBoss(self):
        items = []
        with open("shop.json", "r") as f:
            data = json.load(f)
            items = [item for res in data["res"] if res["villain"] == "boss" for item in res["items"]]
        return items