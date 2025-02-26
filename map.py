import globals, json, init_game
positiveAnswers = ["yes", "y", "ja", "j", "yep", "jop"]
negativeAnswers = ["no", "n", "nein", "ne", "nop", "nope", "nee"]
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
        print("Hier kannst du deine Bauteile zusammenbauen und speichern (wird später implementiert hihi)")
        print("Was möchtest du machen? (Bauteile/Speichern)")
        action = input(">").lower().strip()
        if action == "bauteile":
            if {"Bauteil1", "Bauteil2", "Bauteil3"}.issubset(player.inventory):
                print("Super, du hast alle 3 bauteile gefunden. Als du diese zusammenbaust, merkst du dass es ein schlüssel für die schatzkammer ist, in der du ewigen reichtum findest!")
                print("Herzlichen Glückwunsch du hast das Spiel gewonne :D")
                globals.WINNING = True
            else:
                print("Sorry, dir fehlen wohl teile, gehe auf die Suche um insgesammt 3 Bauteile zu finden")


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

        while (item := input(">").lower().strip()) != "ende":
            if item in shop and (player.inventory["Gutschein"] - shop[item]) >= 0:
                player.inventory["Gutschein"] -= shop[item]
                player.inventory[item] += 1
                print(player.inventory)
            else:
                if item in shop:
                    print("Scheint als hättest du nicht genug Gutscheine")
                else:
                    print("Diesen Artikel haben wir nicht im Angebot")
            print("Du hast noch " + str(player.inventory["Gutschein"]) + " Gutscheine zur verfügung")

class Waterfall:
    def __init__(self, quest):
        self.quest = quest
        self.name = "Wasserfall"
        self.number = 33

    def explore(self, player, rainer):
        rainer.talk(init_game.get_dependencies())
        if rainer.quest.state == "done" and not "Bauteil1" in player.inventory:
            player.inventory["Bauteil1"] += 1
        
class Dam:
    def __init__(self, quest):
        self.quest = quest
        self.name = " Staudamm "        
        self.number = 23

    def explore(self, player, inge):
        inge.talk(init_game.get_dependencies())
        if inge.quest.state == "active" and "Aquarium" in player.inventory:
            player.inventory["Aquarium"] -= 1

class Aquarium:
    def __init__(self, quest):
        self.quest = quest
        self.name = " Aquarium "
        self.number = 31

    def explore(self, player, aquilina):
        aquilina.talk(init_game.get_dependencies())
        if aquilina.quest.state == "done" and aquilina.quest.prev_quest.state == "active" and not "Aquarium" in player.inventory:
           player.inventory["Aquarium"] += 1

class BirdHouse:
    def __init__(self, quest):
        self.quest = quest
        self.name = "Vogelhaus "        
        self.number = 30
        
    def explore(self, tom):
        tom.talk(init_game.get_dependencies())

class Woods:
    def __init__(self, quest):
        self.quest = quest
        self.name = "   Wald   "        
        self.number = 12
        
    def explore(self, berndTheBird):
        berndTheBird.talk(init_game.get_dependencies())
    
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
        if "Bauteil1" in player.inventory and "Bauteil2" in player.inventory:
            player.boss(villains, boss, player)
        else:
            print("Hier passiert noch nichts...")

class EastWoods:
    def __init__(self):
        self.name = "Wald(Ost) "        
        self.number = 13

    def explore(self):
        print("Hier passiert noch nichts...")
