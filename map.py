import globals, json, init_game

class Map:
    def __init__(self, rows, columns):
        self.rows = rows
        self.cols = columns    

    def printMap(self, fields):
        numb, row, col = 10, 10, 0
        topString = "____________"
        sideString = "|          |"
        sideStringNum = "" #later implemented
        bottomString = "|__________|"
        card = [[topString],[sideString],[sideStringNum],[bottomString]]
    
        while row <= self.rows:
            for i in range(len(card)):
                while col < self.cols:
                    if i == 2: #string with num
                        int(numb)
                        numb = col + row
                        strnumb = "          "
                        for field in fields:
                            if field.number == numb:
                                strnumb = field.name
                        card[2][0] = "|" + str(strnumb) + "|"
                    print(card[i][0], end=" ")
                    col += 1
                print()
                col = 0
            row+=10

class Square:
    def __init__(self):
        self.name = "Dorfplatz "
        self.number = 32

    def explore(self, player):
        print("Hier kannst du deine Bauteile zusammenbauen und speichern")
        print(f"Was möchtest du machen? ({globals.COLOR_COMMAND}Bauteile/Speichern\{globals.COLOR_RESET})")
        action = input(f"{globals.COLOR_INPUT}>").lower().strip()
        print(f"{globals.COLOR_RESET}")
        if action == "bauteile":
            if all(player.inventory.has_item(part) for part in {"Bauteil1", "Bauteil2", "Bauteil3"}):
                print("Super, du hast alle 3 bauteile gefunden. Als du diese zusammenbaust, merkst du dass es ein schlüssel für die schatzkammer ist, in der du ewigen reichtum findest!")
                print("Herzlichen Glückwunsch du hast das Spiel gewonne :D")
                globals.WINNING = True
            else:
                print("Sorry, dir fehlen wohl teile, gehe auf die Suche um insgesammt 3 Bauteile zu finden")

        elif action == "speichern":
            quests_dict = {}
            for quest in init_game.quests:
                quests_dict[quest.name] = quest.state.name
            init_game.save_and_load.save(player.positionNow, player.inventory, player.lives, quests_dict)
            print("Dein Spielstand wurde gespeichert!")

class TownHall:
    def __init__(self):
        self.name = " Rathaus  "
        self.number = 42

    def explore(self, player):
        shop = {}
        
        print("Hier kannst du Gutscheine in Ausrüstung tauschen (Tippe 'ende' wenn du fertig bist) \nWir haben im Angebot:")
        with open("shop.json", "r") as f:
            data = json.load(f)
            for res in data["res"]:
                if res["villain"] == "boss":
                    for item in res["items"]:
                        print(f"{item["type"]}: {item["name"]} (-{item["price"]} Gutscheine)\n")
                        shop[item["name"]] = item["price"]

        while (item := input(f"{globals.COLOR_INPUT}>").lower().strip()) != "ende":
            print(f"{globals.COLOR_RESET}")
            if item in shop and (player.inventory["Gutschein"] - shop[item]) >= 0:
                if (item == "schutzschild" or item == "rüstung") and player.inventory.has_item(item):
                    print(f"Du hast bereits diesen Artikel im {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET}")
                else:
                    player.inventory.remove("Gutschein", shop[item])
                    player.inventory.add(item)
                    player.inventory.print_inventory()
            else:
                if item in shop:
                    print("Scheint als hättest du nicht genug Gutscheine")
                else:
                    print("Diesen Artikel haben wir nicht im Angebot")
            print("Du hast noch " + str(player.inventory["Gutschein"]) + " Gutscheine zur verfügung")
        print(f"{globals.COLOR_RESET}")

class Waterfall:
    def __init__(self):
        self.name = "Wasserfall"
        self.number = 33

    def explore(self, player, rainer):
        rainer.talk(init_game.get_dependencies(init_game.quests))
        if rainer.quest.state.name == "done" and not player.inventory.has_item("Bauteil1"):
            player.inventory.add("Bauteil1")
        
class Dam:
    def __init__(self):
        self.name = " Staudamm "        
        self.number = 23

    def explore(self, player, inge):
        inge.talk(init_game.get_dependencies(init_game.quests))
        if inge.quest.state.name == "active" and player.inventory.has_item("Aquarium"):
            player.inventory.remove("Aquarium")

class Aquarium:
    def __init__(self):
        self.name = " Aquarium "
        self.number = 31

    def explore(self, player, aquilina):
        aquilina.talk(init_game.get_dependencies(init_game.quests))
        if aquilina.quest.state.name == "done" and aquilina.quest.prev_quest.state.name == "active" and not player.inventory.has_item("Aquarium"):
           player.inventory.add("Aquarium")

class BirdHouse:
    def __init__(self):
        self.name = "Vogelhaus "        
        self.number = 30
        
    def explore(self, tom):
        tom.talk(init_game.get_dependencies(init_game.quests))

class Woods:
    def __init__(self):
        self.name = "   Wald   "        
        self.number = 12
        
    def explore(self, berndTheBird):
        berndTheBird.talk(init_game.get_dependencies(init_game.quests))
    
class SouthWoods:
    def __init__(self):
        self.name = "Wald(Süd) "        
        self.number = 22

    def explore(self):
        print("Hier passiert noch nichts...")

class WestWoods:
    def __init__(self):
        self.name = "Wald(West)"        
        self.number = 11

    def explore(self, player, villains, boss):
        if player.inventory.has_item("Bauteil1") and player.inventory.has_item("Bauteil2"):
            boss.fight(villains, player)
        else:
            print("Hier passiert noch nichts...")

class EastWoods:
    def __init__(self):
        self.name = "Wald(Ost) "        
        self.number = 13

    def explore(self):
        print("Hier passiert noch nichts...")
