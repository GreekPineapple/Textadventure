import random, json, globals
from collections import Counter
from person import Person
from trivia import *

class Player(Person):
    
    secretPath = False
    
    def __init__(self, lives, strength, name, armmor_points, inventory, positionNow):
        self.armmor_points = armmor_points
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
        fightInventory = ["kick"]
        defencepoints = 1
        specialAttacks = []
        attacks = {}
        swordBonus = False
        strength_bonus = 0
        fire_counter = 0

        # --- Filter attacks and special attacks --- #
        items = self.filterJsonNightServants()
        specialAttacks = [item["name"] for item in items if item["type"] == "Ausweichmanöver"]
        attacks = {item["name"]: 0 for item in items if item["type"] in {"Angriff", "Verteidigung", "Trank"}}

        print("attacks: ", attacks)

        self.shop(fightInventory)
        vc = Counter(fightInventory)
       
        while self.lives > 0 or villain.lives > 0:

            # --- Player attack --- #
            vc = +vc
            print(str(vc).replace("Counter", f"Dein {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} für den Kampf: "))
            choose = self.choose(vc, specialAttacks)
            round = choose[0]
            vc = choose[1]
            
            for angriff in angriffe:
                if angriff.name.lower().strip() == round[0]:
                    print(angriff.make_damage(villain))
                if angriff.name.lower().strip() == round[1]:
                    print(angriff.make_damage(villain))
         
            items = self.filterJsonNightServants()
            for item in items:
                if item["name"] in round:
                    damage, defencepoints, fire_counter = self.checkDamage(item, attacks, villain, defencepoints, swordBonus, strength_bonus, fire_counter, round)
                    villain.lives -= damage
                    attacks[item["name"]] += 1
                    if attacks[item["name"]] > 3:
                        print("\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n")

            if "kick" in round:
                villain.lives -= self.strength
            if fire_counter > 0:
                villain.lives -= 5
                fire_counter -= 1
                print("Gegner brennt und nimmt noch zusätzlich schaden")
            print(f"Der Gegner hat noch {villain.lives} Leben übrig\n")
            
            # --- Villain attack --- #

            for effect in villain.active_effects:
                effect.use(villain)

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
    
    def checkDamage(self,item, attacks, villain, defencepoints, swordBonus, strength_bonus, fire_counter, round):
        damage = 0
        #TODO angriffe als klassen machen
        if item["name"] == "defence":
            value = 0.2 if round[0] == round[1] else 0.1
            defencepoints -= value
            print("defence", defencepoints)
        elif item["type"] == "Trank":
            match item["name"]:
                case "gift":
                    strength_bonus = 0
                case "stärke":
                   strength_bonus = 2
                case "feuer":
                    fire_counter = 3
        elif attacks[item["name"]] > 3:
            print(item["name"], " macht keinen Schaden mehr")
        elif item["name"] == "arrow" and random.random() < 0.10:
            print("Leider hast du daneben geschossen")
        elif round[0] == round[1]:
            print("Solch einen speziellen Angriff zu machen, raubt dir deine Kraft, du verlierts 10 Leben")
            strength_bonus = 2.5
            self.lives -= 10
        elif not swordBonus:
            strength_bonus = 1
        elif swordBonus:
            print("Durch den Angriff des Schwerts in der letzten Runde, macht dein Angriff mehr schaden")
            print(item["name"] + " wurde benutzt")
            strength_bonus = 1.2
            swordBonus = False
        if item["name"] == "sword":
            swordBonus = True
            print("Die Wunde des Gegners heilt sehr langsam, du wirst im Nächsten zug mehr schaden anrichten, wenn du die Wunde triffst.")
        try:
            proof = getattr(villain, f"{item['name']}Proof")
        except AttributeError:
            proof = 0

        damage = (proof + self.strength) * strength_bonus
        return damage, defencepoints, fire_counter

    def shop(self, fightInventory, weapons):
        shop = {}
        print("Willkommen in der Kampfarena. Hier kaufst du Ausrüstung für den Kampf. Währung sind deine eigenen Leben. Die Aurüstung bleibt in der Arena, d.h. was übrig bleibt, landet nicht in deinem Inventar.")
        print("Gewinst du den Kampf, werden deine Leben wieder zurückgesetzt, und du bekommst eine Belohnung. Verlierst du den kampf allerdings, verlierst du 10 Leben außerhalb der Arena.")
        print("Tippe einfach den namen ein, und beende deinen Eimkauf mit 'ende'\n")

        # --- Print items--- #

        for weapon in weapons:
            print(f"{weapon.type}: {weapon.name} (-{weapon.price} Leben) \n{weapon.info}\n")
            shop[weapon.name.lower().strip()] = weapon.price

        while (item := input(f"{globals.COLOR_INPUT}>").lower().strip()) != "ende":
            print(f"{globals.COLOR_RESET}")
            if item == "verteidigung":
                defence = next((weapon for weapon in weapons if weapon.name.lower().strip() == "verteidigung"), None)
                defence.counter -= 1   
            # Wenn man Items schon im shop begrenzen will: (aktuell wird gegner immun; haltbarkeit macht kein sinn)
            # i = [weapon for weapon in weapons if weapon.name.lower().strip() == item]
            # if i.counter != None:
            #   i.counter -= 1
            # if item in shop and i.counter > 0:
            #   self.lives -= shop[item]
            #   fightInventory.append(item)
            #   print("item nichtmehr verfügbar")
            if item in shop:
                if defence.counter >= 0 or item != "verteidigung":
                    self.lives -= shop[item]
                    fightInventory.append(item)
                    print("Du hast noch: " + str(self.lives) + " leben")
                else:
                    print("Du hast schon die maximale ausrüstung für deine Verteidigung")
            else:
                print("Diesen Artikel haben wir nicht im Angebot")
        print(f"{globals.COLOR_RESET}")

    def boss(self, villains, boss, player):
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
        inventory = +Counter({key: self.inventory[key] for key in combinedList})
        print(str(inventory).replace("Counter", f"Dein {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} für den KAMPF: "))

        # --- Phase 1 --- #
        while remainingLayers > 0:
            print(f"Der Gegner hat ein {globals.COLOR_NOUN}Schutzschild{globals.COLOR_RESET} um sich herum, welches nur mit den {globals.COLOR_NOUN}überresten{globals.COLOR_RESET} der besiegten gener zerstört werden kann. Insgesammt gibt es noch {remainingLayers} Schutzschichten. Du kannst nicht zwei schichten mit den gleichen überresten zerstören, und immer nur eine schicht gleichzeitig pro angriff zerstören.\n")
            
            round = self.choose(inventory, [""])
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
        dot_damage = boss.dpw[0]
        while self.lives > 0 or boss.lives > 0:

            # --- Player attack --- #
            round, inventory = self.choose(inventory, [""])
            attacks = round[0]
            items = self.filterJsonBoss()
            paralize = False

            for attack in attacks:
                if attack in [item["name"] for item in items]:
                    if item["name"] == "heiltrank":
                        self.lives = 250
                    if item["name"] == "laehmungstrank":
                        paralize = True
                    if item["type"] == "Schutz":
                        protection += 10
                    boss.lives -= item["damage"]

            print(f"\nGegner Leben: {boss.lives} \n Deine Leben: {self.lives}\n")

            if boss.lives <= 0:
                print("Glückwunsch, Gegner ist tot, hier ist das letzte fehlende Bauteil")
                player.inventory["Bauteil3"] += 1
                break
            
            # --- Villain attack --- #

            if boss.lives <= 90 and dot_rounds == 0:
                dot_rounds = 3
                print("Der Boss hat die hälfte seiner leben verloren, er ist wütend und vergiftet dich. :(")

            if dot_rounds > 0:
                player.lives -= dot_damage
                dot_rounds -= 1
                print(f"Du bist vergiftet! -{dot_damage} Leben.")

            if paralize:
                print("Der Gegner ist gelähmt und kann dich für eine Runde nicht angreifen")
                paralize = False
            else:
                print("Du wirst angegriffen")
                specialAttack = random.random()
                if specialAttack < 0.30: #probabilty of 30% that enemy makes a special attack
                    print("Der gegner nutzt die Energie der Toten Gegner um einen Spezial angruff zu machen. Wehre ihn entweder mit den passenden Überresten ab, oder nutze den Lehmungstrank in der nächsten Runde.")
                    print("Hast du nichts von beiden, bekommst du doppelten Schaden.")
                    round = self.choose(inventory, [""])
                    attacks = round[0]
                    if any(element in attacks for element in protectiveLayer) or "laehmungstrank" in attacks[0]:
                        print("yaay Du whrst den schaden ab")
                    else:
                        print("Der Gegner trifft dch mit mehr schaden :((")
                        self.lives -= (boss.strength - protection) * 1.5 

                else:
                    self.lives -= boss.strength  - protection

                if self.lives <= 0:
                    print("Du wurdest besiegt. Den nächstem Kampf bestreitest du mit 10 Leben weniger.")
                    self.lives = 240
                    break

                print(f"\nGegner Leben: {boss.lives} \n Deine Leben: {self.lives}\n")

    def choose(self, inventory, specialAttacks):
        print(f"Wähle 1-2 Items aus deinem {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} aus, die du nutzen möchtest. Wenn du 2 gleiche Angriffe auswählst, machst du automatisch einen Sepzialangriff. Dieser macht zwar mehr schaden, raubt dir allerdings 10 Leben.")
        print("Wenn du nur 1 Item verwenden willst, tippe beim 2. angriff 'none' ein.")

        # --- First Item --- #

        while (first := input(f"{globals.COLOR_INPUT}1. Angriff: ").lower().strip()) not in inventory or inventory[first] <= 0 or first in specialAttacks:
            print(f"{globals.COLOR_RESET}")
            print("ungültig")
        if not first == "kick":
            inventory[first] -= 1
        inventory = +inventory
        print(f"{globals.COLOR_RESET}")
        print(str(inventory).replace("Counter", f"Dein {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} nach einer Eingabe: ")+"\n")
        
        # --- Second Item --- #

        while (bonus := input(f"{globals.COLOR_INPUT}2. Angriff: ").lower().strip()) != "none" and bonus not in inventory or bonus in specialAttacks:
            print(f"{globals.COLOR_RESET}")
            print("ungültig")
        if not bonus == "kick":
            inventory[bonus] -= 1
        inventory = +inventory
        print(f"{globals.COLOR_RESET}")
        print(str(inventory).replace("Counter", f"Dein {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} nach zwei Eingaben: "))

        round = [first, bonus]

        return round, inventory
    
    def filterJsonNightServants(self):
        items = []
        with open("shop.json", "r") as f:
            data = json.load(f)
            items = [item for res in data["res"] if res["villain"] == "nightServants" for item in res["items"]]
        return items

    def filterJsonBoss(self):
        items = []
        with open("shop.json", "r") as f:
            data = json.load(f)
            items = [item for res in data["res"] if res["villain"] == "boss" for item in res["items"]]
        return items
