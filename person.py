import random, json
from collections import Counter
from trivia import *

class Person:
    def __init__(self, lives, strength, name):
        self.lives = lives
        self.strength = strength
        self.name = name
        
    def printInfo (self):
        print(f"\nDu wirst vom {self.name} angegriffen")
        print(f"Leben: {self.lives}")
        print(f"Stärke: {self.strength}\n" )

class Villain (Person):
    def __init__(self, name, lives, strength, dpw, drop): #Damage Per Weapon (dpw)
        self.waterProof = dpw[0]
        self.arrowProof = dpw[1]
        self.swordProof = dpw[2]
        self.drop = drop
        super().__init__(lives, strength, name)

    def printInfo(self):
        super().printInfo()

class Player(Person):
    
    secretPath = False
    
    def __init__(self, lives, strength, name, inventory, positionNow):
        self.inventory = Counter(inventory)
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
        
        print("In welche Richtung möchtest du gehen? (N/O/S/W)")
        direction = input(">").lower().strip()
        if direction == "n":
            if position == 30:
                if not self.secretPath:
                    print("Hier ist ein geheimweg, den du noch nicht freigeschalten hast!")
                    answer = input("Möchtest du jetzt dein Wissen unter Beweis stellen? (ja/nein)")
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
                    answer = input("Möchtest du jetzt dein Wissen unter Beweis stellen? (ja/nein)")
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

    def fight(self, villain): 
        tempLives = self.lives
        fightInventory = ["kick"]
        defencepoints = 1
        specialAttacks = []
        attacks = {}
        swordBonus = False

        # --- Filter attacks and special attacks --- #
        items = self.filterJsonNightServants()
        for item in items:
            if item["type"] == "Ausweichmanöver":
                specialAttacks.append(item["name"])
            elif item["type"] == "Angriff" or item["type"] == "Verteidigung":
                attacks[item["name"]] = 0

        self.shop(fightInventory)
        vc = Counter(fightInventory)
       
        while self.lives > 0 or villain.lives > 0:

            # --- Player attack --- #
            vc = +vc
            print(str(vc).replace("Counter", "Dein Inventar für den Kampf: "))
            choose = self.choose(vc, specialAttacks)
            round = choose[0]
            vc = choose[1]

            items = self.filterJsonNightServants()
            for item in items:
                if item["name"] in round:
                    damage, defencepoints = self.checkDamage(item, attacks, villain, defencepoints, swordBonus, round)
                    villain.lives -= damage
                    attacks[item["name"]] += 1
                    if attacks[item["name"]] > 3:
                        print("\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n")

            if "kick" in round:
                villain.lives -= self.strength
            print(f"Der Gegner hat noch {villain.lives} Leben übrig\n")
            
            # --- Villain attack --- #
            print("Der Gegner greift dich an")
            isSpecialAttack = random.random()
            if isSpecialAttack < 0.20:
                print("Der gegner macht einen Spezialangriff,")
                if "ausweichmanöver" in vc:
                    print("aber du weichst dem Spezialangriff aus")
                    vc["ausweichmanöver"] -= 1
                else:
                    print("und du wirst getroffen")
                    self.lives -= villain.strength * 2 * defencepoints
                print(f"Deine verbleibenden Leben: {self.lives}\n")
            else:
                self.lives -= villain.strength * defencepoints
                print(f"Deine verbleibenden Leben: {self.lives}\n")
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
    
    def checkDamage(self,item, attacks, villain, defencepoints, swordBonus, round):
        damage = 0
        if item["name"] == "defence":
            value = 0.2 if round[0] == round[1] else 0.1
            defencepoints -= value
            print("defence", defencepoints)
        elif attacks[item["name"]] > 3:
            print(item["name"], " macht keinen Schaden mehr")
        elif item["name"] == "arrow" and random.random() < 0.10:
            print("Leider hast du daneben geschossen")
        elif round[0] == round[1]:
            print("Solch einen speziellen Angriff zu machen, raubt dir deine Kraft, du verlierts 10 Leben")
            damage = (getattr(villain, f"{item["name"]}Proof") + self.strength) * 2.5
            self.lives -= 10
        elif not swordBonus:
            damage = getattr(villain, f"{item["name"]}Proof") + self.strength
        elif swordBonus:
            print("Durch den Angriff des Schwerts in der letzten Runde, macht dein Angriff mehr schaden")
            print(item["name"] + " wurde benutzt")
            damage = getattr(villain, f"{item["name"]}Proof") + 5 + self.strength
            swordBonus = False
        if item["name"] == "sword":
            swordBonus = True
            print("Die Wunde des Gegners heilt sehr langsam, du wirst im Nächsten zug mehr schaden anrichten, wenn du die Wunde triffst.")
        return damage, defencepoints

    def shop(self, fightInventory):
        defenceCount = 0
        shop = {}
        print("Willkommen in der Kampfarena. Hier kaufst du Ausrüstung für den Kampf. Die Aurüstung bleibt in der Arena, d.h. was übrig bleibt, landet nicht in deinem Inventar.")
        print("Gewinst du den Kampf, werden deine Leben wieder zurückgesetzt, und du bekommst eine Belohnung. Verlierst du den kampf allerdings, verlierst du 10 Leben außerhalb der Arena.")
        print("Tippe einfach den namen ein, und beende deinen Eimkauf mit 'ende'\n")

        # --- Print items--- #
        items = self.filterJsonNightServants()
        for item in items:
            print(f"{item["type"]}: {item["name"]} (-{item["price"]} Leben) \n{item["info"]}\n")
            shop[item["name"]] = item["price"]

        while (item := input(">>").lower().strip()) != "ende":
            if item == "defence":
                defenceCount += 1
            if item in shop:
                if defenceCount <= 5 or item != "defence":
                    self.lives -= shop[item]
                    fightInventory.append(item)
                    print("Du hast noch: " + str(self.lives) + " leben")
                else:
                    print("Du darfst nur 5 mal deine Verteidugng verbessern, wähle was anderes aus.")
            else:
                print("Diesen Artikel haben wir nicht im Angebot")

    def boss(self, villains, boss, player):
        remainingLayers = len(villains)
        print("Für den Bosskampf nutzt du die Angriffe aus deinem Inventar und deine tatsächlichen Leben")

        possibleItems = []
        items = self.filterJsonBoss()
        for item in items:
            possibleItems.append(item["name"])

        protectiveLayer = []
        for villain in villains:
            protectiveLayer.append(villain.drop)

        combinedList = set(possibleItems) | set(protectiveLayer)
        inventory = +Counter({key: self.inventory[key] for key in combinedList})
        print(str(inventory).replace("Counter", "Dein Inventar für den KAMPF: "))

        # --- Phase 1 --- #
        while remainingLayers > 0:
            print(f"Der Gegner hat ein Schutzschild um sich herum, welches nur mit den überresten der besiegten gener zerstört werden kann. Insgesammt gibt es noch {remainingLayers} Schutzschichten. Du kannst nicht zwei schichten mit den gleichen überresten zerstören, und immer nur eine schicht gleichzeitig pro angriff zerstören.\n")
            
            round = self.choose(inventory, [""])
            attacks = round[0]

            if attacks[0] in protectiveLayer and attacks[1] in protectiveLayer and attacks[0] != attacks[1]:
                print("die überreste vermischen sich und wirken nicht gegen das schutzschild, hättest du mal zugehört ")

            elif not attacks[0] in protectiveLayer and not attacks[1] in protectiveLayer:
                print("Der Gegner hat eine schutzschicht")
            
            elif any(element in attacks for element in protectiveLayer) or attacks[0] == attacks[1]:
                if attacks[1] != "none" and attacks[0] != attacks[1]:
                    print("Deine normale attacke ist leider nutzlos")
                remainingLayers -=1
                protectiveLayer[:] = [element for element in protectiveLayer if element not in attacks]

                print(f"\nSuper, du hast eine schicht entfernt, es fehlen noch {protectiveLayer}")
         
            print(remainingLayers)
            
        print("Du hast die schutzschicht des gegners gebrochen, jetzt kannst du angreifen")

        # --- Phase 2 --- #
        while self.lives > 0 or boss.lives > 0:

            # --- Player attack --- #
            round = self.choose(inventory, [""])
            attacks = round[0]
            items = self.filterJsonBoss()
            for item in items:
                if item["name"] in round[0]:
                    if item["name"] == "heiltrank":
                        self.lives = 200
                    if item["name"] == "laehmungstrank":
                        pass
                    boss.lives -= item["damage"]

            if boss.lives <= 0:
                print("Glückwunsch, Gegner ist tot, hier ist das letzte fehlende Bauteil")
                player.inventory["Bauteil3"] += 1
                break
            
            # --- Villain attack --- #
            print("Du wirst angegriffen")
            specialAttack = random.random()
            if specialAttack < 0.30: #probabilty of 30% that enemy makes a special attack
                print("Der gegner nutzt die Energie der Toten Gegner um einen Spezial angruff zu machen. Wehre ihn entweder mit den passenden Überresten ab, oder nutze den Lehmungstrank in der nächsten Runde.")
                print("Hast du nichts von beiden, bekommst du doppelten Schaden.")
                round = self.choose(inventory, [""])
                attacks = round[0]
                if any(element in attacks[0] for element in protectiveLayer) or "laehmungstrank" in attacks[0]:
                    print("yaay Du whrst den schaden ab")
                else:
                    print("Der Gegner trifft dch mit doppeltem schaden :((")
                    self.lives -= boss.strength * 2
                    print("Deine Leben: ", self.lives)
            else:
                self.lives -= boss.strength
                print("Deine Leben: ", self.lives)

    def choose(self, inventory, specialAttacks):
        print("Wähle 1-2 Items aus deinem Inventar aus, die du nutzen möchtest. Wenn du 2 gleiche Angriffe auswählst, machst du automatisch einen Sepzialangriff. Dieser macht zwar mehr schaden, raubt dir allerdings 10 Leben.")
        print("Wenn du nur 1 Item verwenden willst, tippe beim 2. angriff 'none' ein.")
        while (first := input("1. Angriff: ").lower().strip()) not in inventory or first in specialAttacks:
            print("ungültig")
        if not first == "kick":
            inventory[first] -= 1
        inventory = +inventory
        print(str(inventory).replace("Counter", "Dein Inventar nach einer Eingabe: "))
        

        while (bonus := input("2. Angriff: ").lower().strip()) != "none" and bonus not in inventory or bonus in specialAttacks:
            print("ungültig")
        if not bonus == "kick":
            inventory[bonus] -= 1
        inventory = +inventory
        print(str(inventory).replace("Counter", "Dein Inventar nach zwei Eingaben: "))

        round = [first, bonus]

        return round, inventory
    
    def filterJsonNightServants(self):
        items = []
        with open("shop.json", "r") as f:
            data = json.load(f)
            for res in data["res"]:
                if res["villain"] == "nightServants":
                    for item in res["items"]:
                        items.append(item)
        return items

    def filterJsonBoss(self):
        items = []
        with open("shop.json", "r") as f:
            data = json.load(f)
            for res in data["res"]:
                if res["villain"] == "boss":
                    for item in res["items"]:
                        items.append(item)
        return items

