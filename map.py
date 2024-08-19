import globals, json
positiveAnswers = ["yes", "y", "ja", "j", "yep", "jop"]
negativeAnswers = ["no", "n", "nein", "ne", "nop", "nope", "nee"]
class Map:
    def __init__(self, rows, columns):
        self.rows = rows
        self.cols = columns
        
    def addFieldName(self, numb):
        match numb:
            case 1 | 5 | 6 | 13 | 14 | 16:
                numb = "          "
            case 2 | 3 | 4 | 7:
                numb = "   Wald   "
            case 8:
                numb = " Staudamm "
            case 9:
                numb = "Vogelhaus "
            case 10:
                numb = " Aquarium "
            case 11:
                numb = "Dorfplatz "
            case 12:
                numb = "Wasserfall"
            case 15:
                numb = " Rathaus  "
            case _:
                numb = "    " + str(numb) + "    "
        return numb

    def printMap(self):
        row = col = numb = 0
        topString = "____________"
        sideString = "|          |"
        sideStringNum = "" #later implemented
        bottomString = "|__________|"
        card = [[topString],[sideString],[sideStringNum],[bottomString]]
    
        while row < self.rows:
            for i in range(len(card)):
                while col < self.cols:
                    if i == 2: #string with num
                        int(numb)
                        numb+=1
                        strnumb = str(numb)
                        strnumb = self.addFieldName(numb)
                        card[2][0] = "|" + str(strnumb) + "|"
                    print(card[i][0], end=" ")
                    col += 1
                print()
                col = 0
            row+=1

class Square:
    def explore(self, player):
        print("Hier kannst du deine Bauteile zusammenbauen und speichern (wird später implementiert hihi)")
        print("Was möchtest du machen? (Bauteile/Speichern)")
        action = input(">").lower().strip()
        if action == "bauteile":
            if {"Bauteil1", "Bauteil2", "Bauteil3"}.issubset(player.inventory):
                print("Super, du hast alle 3 bauteile gefunden. Als du diese zusammenbaust, merkst du dass es ein schlüssel für die schatzkammer ist, in der du ewigen reichtum findest!")
                print("Herzlichen Glückwunsch du hast das Spiel gewonne :D")
                globals.winning = True
            else:
                print("Sorry, dir fehlen wohl teile, gehe auf die Suche um insgesammt 3 Bauteile zu finden")


class TownHall:
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
    
    def explore(self, damquest, note, player):
        if self.quest == "open":
            print('Rainer: "Oh man, hier war mal ein schöner Wasserfall, aber irgenjemand musste ja unbedingt ein Staudamm in Richtung Norden bauen...')
            print('Kannst du der Sache auf den Grund gehen?"')
            option = input(">").lower().strip()
            if option in positiveAnswers:
                print("Gehe nach Norden und schau dich da mal um.")
                self.quest = "active"
                note.write(" - Sieh dich im Norden um")
            elif option in negativeAnswers:
                print('Rainer: "Okay schade, vielleicht ja später!"')
            else:
                print("ungültige eingabe")
        elif self.quest == "active":
            if damquest == "done":
                print('Rainer: "Woow, der Wasserfall fließt wieder, jetzt kann ich ganz entspannt meine Mittagspause hier verbingen')
                print('Du erhälst dafür eine kleine Belohnung von mir, hoffe du kannst damit was anfangen"')
                # erstes Bauteil geben
                player.inventory["Bauteil1"] += 1
                self.quest = "done"
                note.delete(" - Rede mit Rainer am Wasserfall")
            else:
                print("Schon im Norden umgeschauet?")
        elif self.quest == "done":
            print("Diese Quest wurde schon beendet! ;)")
        return self.quest
        
class Dam:
    def __init__(self, quest):
        self.quest = quest 

    def explore(self, wfquest, aqquest, player, note):
        if self.quest == "open":
            print("Hier ist eine Frau die Fische füttert")
            if wfquest == "active":
                print('Inge: "Durch den Damm den ich gebaut habe, sind die Fische endlich sicher und ich kann mich gut um sie kümmern."')
                print('A: "Der Wasserfall ist aber total ausgetrocknet!"')
                print('B: "Darf ich auch mal Füttern?"')
                print('C: "Okay, dann viel Spaß noch."')
                option = input(">").capitalize().strip()
                if option == "A":
                    print('Inge: "Ich würde dir ja gerne helfen, aber die Fische brauchen einen Ort zum Leben. Wenn es doch nur irgendwie einen weg geben würde, ein Aquarium zu besorgen..."')
                    self.quest = "active"
                    note.delete(" - Sieh dich im Norden um")
                    note.write(" - Besorge ein Aquarium")
                elif option == "B":
                    print("*Fütter*")

        elif self.quest == "active":
            if aqquest == "done":
                print("Super, jetzt kann ich die fische bei mir zuhause versorgen")
                self.quest = "done"
                player.inventory["Aquarium"] -= 1
                note.delete(" - Gehe zu der Frau am Staudamm und übergib ihr das Aquarium für ihre Fische")
                note.write(" - Rede mit Rainer am Wasserfall")
            else:
                print("Besorge ein AAquarium um die Fische zu retten")

        elif self.quest == "done":
            print('Inge: "Der Wasserfall geht ja ganz schön tief"')
            
        return self.quest

class Aquarium:
    def __init__(self, quest):
        self.quest = quest 

    def explore(self, damquest, birdquest, player, note):
        
        if self.quest == "open": 
            if damquest == "active":
                print("Wilkommmen bei Aquilinas Aquarium Laden! *(kurz: AAL)*")
                print("Was kann ich für dich tun?")
                option = input(">").lower().strip()
                if "aquarium" in option:
                    print("Ah, du interessierst dich für unsere Aquarien?")
                    option = input(">").lower().strip()
                    if option in positiveAnswers:
                        print("Ich kann dir ein Angebot machen: Mein Kollege von der Vogelzucht braucht hilfe mit einem seiner Vögel...")
                        print("Er hat mich gebeten ihm zu helfen, doch ich habe einfach keine zeit. Wenn du ihm stattdessen hilfst, bekommst du ein Aquaium umsonst. Frage dort nach, was genau du tun kannst.")
                        print("Würdest du mir diesen gefallen tun?")
                        option = input(">").lower().strip()
                        if option in positiveAnswers:
                            self.quest = "active"
                            note.delete(" - Besorge ein Aquarium")
                            note.write(" - Gehe zum Vogelhaus um rauszufinden wo sich der Vogel versteckt")
                    else:
                        pass
                else:
                    print("Mit dieser Sache kann ich dir leider nicht weiterhelfen.")
            else:
                print("Hier ist ein Aquarium shop. Er scheint aber geschlossen zu sein...")
        elif self.quest == "active":
            if birdquest == "done":
                print("Hast du den Vogel gefunden und zurück gebracht?")
                option = input(">").lower().strip()
                if option in positiveAnswers:
                    print("Super, vielen Dank! Hier bekommst du ein Aquarium")
                    player.inventory["Aquarium"] += 1
                    self.quest = "done"
                    note.delete(" - Gehe zum Aquarium shop und hohle dir ein Aquarium")
                    note.write(" - Gehe zu der Frau am Staudamm und übergib ihr das Aquarium für ihre Fische")
            else:
                print("Finde den Vogel und bringe ihn zum Vogelhaus, um dir später hier ein Aquarium abzuholen!")
        elif self.quest == "done":
            print("Wilkommmen bei Aquilinas Aquarium Laden! *(kurz: AAL)*")
            print("Was kann ich für dich tun?")
            
        return self.quest

class BirdHouse:
    def __init__(self, quest):
        self.quest = quest 
        
    def explore(self, aqquest, birdquest, note):
        if self.quest == "open":
            if aqquest == "active":
                print("Leider ist mir unser schönster Vogel abgehauen, aber mein kollege und ich suchen grade zusammen nach ihm") 
                print("Kannst du uns vielleicht dabei helfen?")
                answer = input(">").lower().strip()
                if answer in positiveAnswers: 
                    print("Mega, danke! Vermutlich wird er sich irgendwo im Wald aufhalten, aber sicher bin ich mir da nicht..")
                    self.quest = "active"
                    note.delete(" - Gehe zum Vogelhaus um rauszufinden wo sich der Vogel versteckt")
                    note.write(" - Suche den Vogel und bringe ihn in das Vogelzucht haus")
            else:
                print("Hier Vogelhaus")

        elif self.quest == "active":
            if birdquest == "done":
                print("Wilkommmen bei der Vogelzucht")
                print("wie ich sehe hast du meinen Vogel gefunden?")
                answer = input(">").lower().strip()
                if answer in positiveAnswers:
                    print("Super, vielen Dank!")
                    print("Kannst du noch bei mienem Kollegen im Aquarium shop vorbei schauen und sagen, der Vogel ist wieder da? Danke!")
                    self.quest = "done"
                    note.delete(" - Bringe den Vogel in das Vogelzucht haus")
                    note.write(" - Gehe zum Aquarium shop und hohle dir ein Aquarium")
                else:
                    print("ungültige eingabe")
            else:
                print("Der Vogel sollte sich irgendwo im Wald verstecken")
        elif self.quest == "done":
            print("Wilkommmen bei der Vogelzucht noch kannst du hier nichts machen, außer den ausreißer betrachten")
        return self.quest

class Woods:
    def __init__(self, quest):
        self.quest = quest 
        
    def explore(self, birdquest, note):
        if self.quest == "open":
            if birdquest == "active":
                print("Das hier muss der Vogel sein der weggeflogen ist... \nAber wie fang ich ihn am besten?")
                print("A: Vogelgeräusche imitieren \nB: Warten bis der Vogel weiter runter fliegt und ihn dann fangen \nC: Auf den Baum klettern und ihn fangen")
                option = input(">").lower().strip()
                if option == "a":
                    print("Der Vogel denkt du bist ein Angreifer, du stirbst...")
                elif option == "b":
                    print("Glükwunssch du hast in gefangen")
                    self.quest = "done"
                    note.delete(" - Suche den Vogel und bringe ihn in das Vogelzucht haus")
                    note.write(" - Bringe den Vogel in das Vogelzucht haus")
                elif option == "c":
                    print("Du bist vom Baum gefallen und gestorben, lol")
        return self.quest
    
class SouthWoods:
    def explore(self):
        print("Hier passiert noch nichts...")

class WestWoods:
    def explore(self, player, villains, boss):
        if "Bauteil1" in player.inventory and "Bauteil2" in player.inventory:
            player.boss(villains, boss, player)
        else:
            print("Hier passiert noch nichts...")

class EastWoods:
    def explore(self):
        print("Hier passiert noch nichts...")