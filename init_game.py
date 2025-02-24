from state_quest import *
from person import NPC, Villain
from player import Player
from map import *
from notes import *
from state_quest import *

# Notes

notes = Notes()

# Map

map = Map(40,4)
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

fields = [townhall, woods, wf, dam, aquarium, square, birdhouse, ww, ew, sw]

# Characters

me = Player(200, 10, "myself", [], 42) #Start: Townhall

goblin = Villain("Goblin", 90, 35, [10, 20, 15], "goblin überreste")
golem = Villain("Erdgolem", 140, 50, [20, 20, 10], "golem überreste")
wizard = Villain("Magier", 135, 40,[10, 20, 10], "wizard überreste")
luftGegner = Villain("Luftgegner", 110, 30,[5, 20, 0], "vogel überreste")

boss = Villain("Boss", 150, 150, ["a","b","c"], "special glitzer boss attacke")

villains = [goblin, golem, wizard, luftGegner]

# Quests

quest1 = state_quest("Wasserfallquest", " - Sieh dich im Norden um", "", notes)
quest2 = state_quest("Staudammquest", "Besorge ein Aquarium damit der Staudamm entfernt werden kann")
quest3 = state_quest("Aquariumquest", "Hilf dem Kollegen um ein Aquarium zu bekommen")
quest4 = state_quest("Birdhousequest", "Such den Vogel und hold dir dein Aquarium ab!")
quest5 = state_quest("Vogelquest", "Fange den Vogel ein")

# NPCs

rainer = NPC("Rainer", 100, 5, quest1, {
    "open": {
        "ready": "Oh man, hier war mal ein schöner Wasserfall, aber irgenjemand musste ja unbedingt ein Staudamm in Richtung Norden bauen..."
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Woow, der Wasserfall fließt wieder, jetzt kann ich ganz entspannt meine Mittagspause hier verbingen!\nDu erhälst dafür eine kleine Belohnung von mir, hoffe du kannst damit was anfangen quest_done",
        "blocked": "Schon im Norden umgeschauet?"
    },
    "done": "Danke! Jetzt fließt das Wasser wieder!"
}, {
    "open1": {
        "question": "Kannst du der Sache auf den Grund gehen? (ja/nein)",
        "ja": "Gehe nach Norden und schau dich da mal um. quest_start",
        "nein": "Okay schade, vielleicht ja später!"
    }
})

inge = NPC("Inge", 100, 5, quest2, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Durch den Damm den ich gebaut habe, sind die Fische endlich sicher und ich kann mich gut um sie kümmern.",
        "blocked": "Hier ist eine Frau die Fische füttert"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Super, jetzt kann ich die fische bei mir zuhause versorgen quest_done",
        "blocked": "Besorge ein Aquarium um die Fische zu retten"
    },
    "done": "Der Wasserfall geht ja ganz schön tief!"
}, {
    "open1": {
        "question": "A: Der Wasserfall ist aber total ausgetrocknet!\nB: Darf ich auch mal Füttern?\nC: Okay, dann viel Spaß noch.",
        "a": "Ich würde dir ja gerne helfen, aber die Fische brauchen einen Ort zum Leben. Wenn es doch nur irgendwie einen weg geben würde, ein Aquarium zu besorgen... quest_start",
        "b": "*Fütter*",
        "c": "Danke"
    }
})

aquilina = NPC("Aquilina", 100, 5, quest3, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Wilkommmen bei Aquilinas Aquarium Laden! *(kurz: AAL)*",
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
        "question": "Würdest du mir diesen gefallen tun? (ja/nein)\n",
        "ja": "Super, frage einfach bei der Vogelzucht nach, was genau du tun kannst. quest_start",
        "nein": "Schade, vielleicht ja später."
    },
    "active3": { 
        "question": "Hast du den Vogel gefunden und zurück gebracht? (ja/nein)\n",
        "ja": "Super, vielen Dank! Hier bekommst du ein Aquarium. quest_done",
        "nein": "Dann such mal weiter!"
    }
})

tom = NPC("Tom", 100, 5, quest4, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Leider ist mir unser schönster Vogel abgehauen. Er ist krank und braucht hilfe, aber mein kollege und ich suchen grade zusammen nach ihm",
        "blocked": "Hier Vögel, da Vögel, überall Vögel!"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Hi, wie gehts?",
        "blocked": "Der Vogel sollte sich irgendwo im Wald verstecken!"
    },
    "done": "Wilkommmen bei der Vogelzucht noch kannst du hier nichts machen, außer den ausreißer betrachten"
}, {
    "open1": {
        "question": "Kannst du uns vielleicht dabei helfen?(ja/nein)\n",
        "ja": "Mega, danke! Vermutlich wird er sich irgendwo im Wald aufhalten, aber sicher bin ich mir da nicht... quest_start",
        "nein": "Dann entschuldige mich, ich muss meinen Vogel finden!"
    },
    "active2": { 
        "question": "Wie ich sehe hast du meinen Vogel gefunden?(ja/nein)",
        "ja": "Super, vielen Dank!\nKannst du noch bei mienem Kollegen im Aquarium shop vorbei schauen und sagen, der Vogel ist wieder da? Danke! quest_done",
        "nein": "Dann such mal weiter!"
    }
})

berndTheBird = NPC("Bernd the Bird", 100, 5, quest5, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Das hier muss der Vogel sein der weggeflogen ist... \nAber wie fang ich ihn am besten? quest_start",
        "blocked": "Schöner Wald hier :)"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Dann versuche ich noch einmal den Vogel einzufangen!"
    },
    "done": "Dem Vogel geht es jetzt bestimmt besser!"
}, {
    "open1": {
        "question": "A: Vogelgeräusche imitieren \nB: Warten bis der Vogel weiter runter fliegt und ihn dann fangen \nC: Auf den Baum klettern und ihn fangen",
        "a": "Der Vogel denkt du bist ein Angreifer, du stirbst...",
        "b": "Glükwunssch du hast in gefangen quest_done",
        "c": "Du bist vom Baum gefallen und gestorben, lol"
    },
})

def get_dependencies():
    return {
        "Wasserfallquest": "ready",
        "Staudammquest": "ready" if quest1.state == "active" else "blocked",
        "Aquariumquest": "ready" if quest2.state == "active" else "blocked",
        "Birdhousequest": "ready" if quest3.state == "active" else "blocked",
        "Vogelquest": "ready" if quest4.state == "active" else "blocked",
        "Vogelquest_done": "ready",
        "Birdhousequest_done": "ready" if quest5.state =="done" else "blocked",
        "Aquariumquest_done": "ready" if quest4.state == "done" else "blocked",
        "Staudammquest_done": "ready" if quest3.state == "done" else "blocked",
        "Wasserfallquest_done": "ready" if quest2.state == "done" else "blocked",
    }