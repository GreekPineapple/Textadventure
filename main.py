import random, globals
from person import NPC, Villain
from player import Player
from map import *
from notes import *
from state_quest import *
map = Map(40,4)
me = Player(200, 10, "myself", [], 42) #Start: Townhall
notes = Notes()
townhall = TownHall()
woods = Woods("open")
wf = Waterfall("open")
dam = Dam("open")
aquarium = Aquarium("open")
square = Square()
birdhouse = BirdHouse("open")
ww = WestWoods()
sw = SouthWoods()
ew = EastWoods()

goblin = Villain("Goblin", 90, 35, [10, 20, 15], "goblin überreste")
golem = Villain("Erdgolem", 140, 50, [20, 20, 10], "golem überreste")
wizard = Villain("Magier", 135, 40,[10, 20, 10], "wizard überreste")
luftGegner = Villain("Luftgegner", 110, 30,[5, 20, 0], "vogel überreste")

boss = Villain("Boss", 150, 150, ["a","b","c"], "special glitzer boss attacke")

villains = [goblin, golem, wizard, luftGegner]
fields = [townhall, woods, wf, dam, aquarium, square, birdhouse, ww, ew, sw]


quest1 = state_quest("Wasserfallquest", "Entferne den Staudamm damit der Wasserfall wieder fließen kann")
quest2 = state_quest("Staudammquest", "Besorge ein Aquarium damit der Staudamm entfernt werden kann")
quest3 = state_quest("Aquariumquest", "Hilf dem Kollegen um ein Aquarium zu bekommen")
quest4 = state_quest("Birdquest", "Such den Vogel und hold dir dein Aquarium ab!")
quest5 = state_quest("Vogelquest", "Fange den Vogel ein")

rainer = NPC("Rainer", 100, 5, "nothing", quest1, {
    "open": {
        "ready": "Oh man, hier war mal ein schöner Wasserfall, aber irgenjemand musste ja unbedingt ein Staudamm in Richtung Norden bauen...\nKannst du der Sache auf den Grund gehen? (ja/nein)"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Woow, der Wasserfall fließt wieder, jetzt kann ich ganz entspannt meine Mittagspause hier verbingen!\nDu erhälst dafür eine kleine Belohnung von mir, hoffe du kannst damit was anfangen",
        "blocked": "Schon im Norden umgeschauet?"
    },
    "done": "Danke! Jetzt fließt das Wasser wieder!"
}, {
    "open": {
        "ja": "Gehe nach Norden und schau dich da mal um.",
        "nein": "Okay schade, vielleicht ja später!"
    }
})

inge = NPC("Inge", 100, 5, "nothing", quest2, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Durch den Damm den ich gebaut habe, sind die Fische endlich sicher und ich kann mich gut um sie kümmern.\nA: Der Wasserfall ist aber total ausgetrocknet!\nB: Darf ich auch mal Füttern?\nC: Okay, dann viel Spaß noch.",
        "blocked": "Hier ist eine Frau die Fische füttert"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Super, jetzt kann ich die fische bei mir zuhause versorgen",
        "blocked": "Besorge ein Aquarium um die Fische zu retten"
    },
    "done": "Der Wasserfall geht ja ganz schön tief!"
}, {
    "open": {
        "a": "Ich würde dir ja gerne helfen, aber die Fische brauchen einen Ort zum Leben. Wenn es doch nur irgendwie einen weg geben würde, ein Aquarium zu besorgen...",
        "b": "*Fütter*",
        "c": "Danke"
    }
})

aquilina = NPC("Aquilina", 100, 5, "nothing", quest3, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Wilkommmen bei Aquilinas Aquarium Laden! *(kurz: AAL)*\n",
        "blocked": "Hier ist ein Aquarium shop. Er scheint aber geschlossen zu sein..."
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "",
        "blocked": "Finde den Vogel und bringe ihn zum Vogelhaus, um dir später hier ein Aquarium abzuholen!"
    },
    "done": "Wilkommmen bei Aquilinas Aquarium Laden! *(kurz: AAL)*"
}, {
    "open1": {
        "question": "Was kann ich für dich tun?\nA: Ich interessiere mich für ein Aquarium.\nB: Ich möchte Fische kaufen\nC: Nichts.",
        "a": "Ich kann dir ein Angebot machen: Mein Kollege von der Vogelzucht braucht hilfe mit einem seiner Vögel...\nEr hat mich gebeten ihm zu helfen, doch ich habe einfach keine zeit. Wenn du ihm stattdessen hilfst, bekommst du ein Aquarium umsonst.",
        "b": "Dann schau dich gerne um, ich habe eine große Auswahl an Fischen.",
        "c": "Okay, bis bald."
    },
    "open2": { 
        "question": "Würdest du mir diesen gefallen tun? (ja/nein)",
        "ja": "Super, frage einfach bei der Vogelzucht nach, was genau du tun kannst.",
        "nein": "Schade, vielleicht ja später."
    },
    "active3": { 
        "question": "Hast du den Vogel gefunden und zurück gebracht? (ja/nein)",
        "ja": "Super, vielen Dank! Hier bekommst du ein Aquarium.",
        "nein": "Dann such mal weiter!"
    }
})

tom = NPC("Tom", 100, 5, "nothing", quest4, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Leider ist mir unser schönster Vogel abgehauen. Er ist krank und braucht hilfe, aber mein kollege und ich suchen grade zusammen nach ihm",
        "blocked": "Hier Vögel, da Vögel, überall Vögel!"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Hi, wie ich sehe hast du meinen Vogel gefunden?(ja/nein)",
        "blocked": "Der Vogel sollte sich irgendwo im Wald verstecken!"
    },
    "done": "Wilkommmen bei der Vogelzucht noch kannst du hier nichts machen, außer den ausreißer betrachten"
}, {
    "open1": {
        "question": "Kannst du uns vielleicht dabei helfen?(ja/nein)",
        "ja": "Mega, danke! Vermutlich wird er sich irgendwo im Wald aufhalten, aber sicher bin ich mir da nicht..",
        "nein": "Dann entschuldige mich, ich muss meinen Vogel finden!"
    },
    "active2": { 
        "question": ">",
        "ja": "Super, vielen Dank!\nKannst du noch bei mienem Kollegen im Aquarium shop vorbei schauen und sagen, der Vogel ist wieder da? Danke!",
        "nein": "Dann such mal weiter!"
    }
})

berndTheBird = NPC("Bernd the Bird", 100, 5, "nothing", quest5, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Das hier muss der Vogel sein der weggeflogen ist... \nAber wie fang ich ihn am besten?",
        "blocked": "Schöner Wald hier :)"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Dann versuche ich noch einmal den Vogel einzufangen!",
        "blocked": ""
    },
    "done": "Dem Vogel geht es jetzt bestimmt besser!"
}, {
    "open1": {
        "question": "A: Vogelgeräusche imitieren \nB: Warten bis der Vogel weiter runter fliegt und ihn dann fangen \nC: Auf den Baum klettern und ihn fangen\n>",
        "a": "Der Vogel denkt du bist ein Angreifer, du stirbst...",
        "b": "Glükwunssch du hast in gefangen",
        "c": "Du bist vom Baum gefallen und gestorben, lol"
    },
})
def get_dependencies():
    return {
        "Wasserfallquest": "ready",
        "Staudammquest": "ready" if quest1.state == "active" else "blocked",
        "Wasserfallquest_done": "ready" if quest2.state == "done" else "blocked",
        "Aquariumquest": "ready" if quest2.state == "active" else "blocked",
        "Staudammquest_done": "ready" if quest3.state == "done" else "blocked",
        "Aquariumquest_done": "ready" if quest1.state == "done" else "blocked"
    }

quest1.start()
quest2.start()
quest3.start()
aquilina.talk(get_dependencies())


# rainer.talk(get_dependencies())
# quest1.start()
# inge.talk(get_dependencies())
# quest2.start()
# aquilina.talk(get_dependencies())
# quest3.start()
# rainer.talk(get_dependencies())
# quest2.complete()
# rainer.talk(get_dependencies())


def checkAction(position):
    match position:
        case 11:
            ww.explore(me, villains, boss)
        case 12:
            pass
        case 13:
            pass
        case 22:
            woods.quest = woods.explore(birdhouse.quest, notes)
        case 23:
            dam.quest = dam.explore(wf.quest, aquarium.quest, me, notes)
        case 30:
            birdhouse.quest = birdhouse.explore(aquarium.quest, woods.quest, notes)
        case 31:
            aquarium.quest = aquarium.explore(dam.quest, birdhouse.quest, me, notes)
        case 32:
            square.explore(me)
        case 33:
            wf.quest = wf.explore(dam.quest, notes, me)
        case 42:
            townhall.explore(me)

def printposition(position):
    for field in fields:
        if field.number == position:
            print(f"--{field.name.strip()}--")

def lookAround(block):
    fight = random.choices((True, False), weights = [1, 3])
    if fight[0] and not block:
        villain = random.choice(villains)
        villain.printInfo()
        if input("Nimmst du den Kampf an?").lower().strip() == "ja":
            me.fight(villain)
        block = not block
    else:       
        checkAction(me.positionNow)
        block = not block
    return block

# quest can be: open; active; done; 

map.printMap(fields)
notes.read()

block = False # avoids two fights after another

while me.lives > 0:
    if globals.winning:
        print("Yaay du hast gewonnen")
        break
    print("Was möchtest du machen?")
    doing = input(">").lower().strip()
    if doing == "umschauen":
        block = lookAround(block)
    elif doing == "laufen":
        me.move(wf.quest)
        printposition(me.positionNow)
    elif doing == "inventar":
        print(me.inventory)
    elif doing == "help":
        notes.read()
    elif doing == "map":
        map.printMap()
    elif doing == "ende":
        break
    else:
        print("ungültige eingabe")
print("GAME OVER!")