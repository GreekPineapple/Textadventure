def addFieldName(numb):
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

def printMap(cols, rows):
    row = col = numb = 0
    topString = "____________"
    sideString = "|          |"
    sideStringNum = "" #later implemented
    bottomString = "|__________|"
    card = [[topString],[sideString],[sideStringNum],[bottomString]]
  
    while row < rows:
        for i in range(len(card)):
            while col < cols:
                if i == 2: #string with num
                    int(numb)
                    numb+=1
                    strnumb = str(numb)
                    strnumb = addFieldName(numb)
                    card[2][0] = "|" + str(strnumb) + "|"
                print(card[i][0], end=" ")
                col += 1
            print()
            col = 0
        row+=1

printMap(4, 4)

class Square:
    def explore(self):
        pass

class TownHall:
    def explore(self):
        pass

class Waterfall:
    def __init__(self, quest):
        self.quest = quest
    
    def explore(self, damquest, note):
        if self.quest == "open":
            print('Rainer: "Oh man, hier war mal ein schöner Wasserfall, aber irgenjemand musste ja unbedingt ein Staudamm in Richtung Norden bauen...')
            print('Kannst du der Sache auf den Grund gehen?" (yes / no)')
            option = input(">")
            if option.lower() == "yes":
                print("Gehe nach Norden und schau dich da mal um.")
                self.quest = "active"
                note.write(" - Sieh dich im Norden um")
            elif option.lower() == "no":
                print('Rainer: "Okay schade, vielleicht ja später!"')
            else:
                print("ungültige eingabe")
        elif self.quest == "active":
            if damquest == "done":
                print('Rainer: "Woow, der Wasserfall fließt wieder, jetzt kann ich ganz entspannt meine Mittagspause hier verbingen')
                print('Du erhälst dafür eine kleine Belohnung von mir, hoffe du kannst damit was anfangen"')
                # erste Trank zutat geben
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
                option = input(">")
                if option.capitalize() == "A":
                    print('Inge: "Ich würde dir ja gerne helfen, aber die Fische brauchen einen Ort zum Leben. Wenn es doch nur irgendwie einen weg geben würde, ein Aquarium zu besorgen..."')
                    self.quest = "active"
                    note.delete(" - Sieh dich im Norden um")
                    note.write(" - Besorge ein Aquarium")
                elif option.capitalize() == "B":
                    print("*Fütter*")

        elif self.quest == "active":
            if aqquest == "done":
                print("Super, jetzt kann ich die fische bei mir zuhause versorgen")
                self.quest = "done"
                player.inventory.remove("Aquarium")
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
                option = input(">")
                if "aquarium" in option.lower():
                    print("Ah, du interessierst dich für unsere Aquarien? (yes/no)")
                    option = input(">")
                    if option.lower() == "ja" or "j" or "yes" or "y":
                        print("Ich kann dir ein Angebot machen: Mein Kollege von der Vogelzucht hat einen ausreiser...")
                        print("Er hat mich gebeten ihn bei der Suche zu helfen, doch ich habe einfach keine zeit. Wenn du den Vogel zurück in die Vogelzucht bringst, bekommst du ein Aquaium umsonst. Frage dort nach, wo du suchen musst.")
                        print("Hilfst du mir? (yes / no)")
                        option = input(">")
                        if option.lower() == "yes":
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
                print("Hast du den Vogel gefunden und zurück gebracht? (yes/no)")
                option = input(">")
                if option.lower() == "yes":
                    print("Super, vielen Dank! Hier bekommst du ein Aquarium")
                    player.inventory.append("Aquarium")
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
                print("Kannst du uns vielleicht dabei helfen? (yes/no)")
                answer = input(">")
                if answer == "yes": 
                    print("Mega, danke! Vermutlich wird er sich irgendwo im Wald aufhalten, aber sicher bin ich mir da nicht..")
                    self.quest = "active"
                    note.delete(" - Gehe zum Vogelhaus um rauszufinden wo sich der Vogel versteckt")
                    note.write(" - Bringe den Vogel in das Vogelzucht haus")
            else:
                print("Hier Vogelhaus")

        elif self.quest == "active":
            if birdquest == "done":
                print("Wilkommmen bei der Vogelzucht")
                print("wie ich sehe hast du meinen Vogel gefunden? (yes)")
                answer = input(">")
                if answer == "yes":
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
                option = input(">")
                if option.lower() == "a":
                    print("Der Vogel denkt du bist ein Angreifer, du stirbst...")
                elif option.lower() == "b":
                    print("Glükwunssch du hast in gefangen")
                    self.quest = "done"
                    note.delete(" - Suche den Vogel und bringe ihn in das Vogelzucht haus")
                    note.write(" - Bringe den Vogel in das Vogelzucht haus")
                elif option.lower() == "c":
                    print("Du bist vom Baum gefallen und gestorben, lol")
        return self.quest
class SouthWoods:
    def explore(self):
        pass

class WestWoods:
    def explore(self):
        pass

class EastWoods:
    def explore(self):
        pass