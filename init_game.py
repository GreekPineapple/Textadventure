from quest import *
from person import NPC, Villain
from player import Player
from map import *
from notes import *
from states import *
from state_manager import Statemanager
from save_and_load import SaveAndLoad

# --- Notes --- #

notes = Notes()
save_and_load = SaveAndLoad()

# --- Map --- #

map = Map(40,4)
townhall = TownHall()
woods = Woods()
wf = Waterfall()
dam = Dam()
aquarium = Aquarium()
square = Square()
birdhouse = BirdHouse()
ww = WestWoods()
sw = SouthWoods()
ew = EastWoods()

fields = [townhall, woods, wf, dam, aquarium, square, birdhouse, ww, ew, sw]

# --- Characters --- #

me = Player(save_and_load.load()["lives"], 10, "myself", save_and_load.load()["inventory"], save_and_load.load()["position"]) #Start: Townhall

goblin = Villain("Goblin", 90, 35, [10, 20, 15], "goblin überreste")
golem = Villain("Erdgolem", 140, 50, [20, 20, 10], "golem überreste")
wizard = Villain("Magier", 135, 40,[10, 20, 10], "wizard überreste")
luftGegner = Villain("Luftgegner", 110, 30,[5, 20, 0], "vogel überreste")

boss = Villain("Boss", 150, 150, ["a","b","c"], "special glitzer boss attacke")

villains = [goblin, golem, wizard, luftGegner]

# --- States --- #

state_manager = Statemanager()
state_manager.add(OpenState())
state_manager.add(ActiveState())
state_manager.add(DoneState())

# --- Quests --- #

quest1 = Quest("Wasserfallquest", " - Sieh dich im Norden um", "", notes, state_manager, prev_quest=None)
quest2 = Quest("Staudammquest", " - Besorge ein Aquarium", " - Rede mit Rainer am Wasserfall", notes, state_manager, prev_quest=quest1)
quest3 = Quest("Aquariumquest", " - Gehe zum Vogelhaus um rauszufinden wo sich der Vogel versteckt"," - Gehe zu der Frau am Staudamm und übergib ihr das Aquarium für ihre Fische", notes, state_manager, prev_quest=quest2)
quest4 = Quest("Birdhousequest", " - Suche den Vogel und bringe ihn in das Vogelzucht haus"," - Gehe zum Aquarium shop und hohle dir ein Aquarium", notes, state_manager, prev_quest=quest3)
quest5 = Quest("Vogelquest", " - Fange den Vogel"," - Bringe den Vogel in das Vogelzucht haus", notes, state_manager, prev_quest=quest4)

quests = [quest1, quest2, quest3, quest4, quest5]

# --- NPCs --- #

rainer = NPC("Rainer", 100, 5, quest1, {
    "open": {
        "ready": "Oh man, hier war mal ein schöner Wasserfall, aber irgenjemand musste ja unbedingt ein Staudamm in Richtung Norden bauen..."
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Woow, der Wasserfall fließt wieder, jetzt kann ich ganz entspannt meine Mittagspause hier verbingen!",
        "blocked": "Schon im Norden umgeschauet?"
    },
    "done": "Danke! Jetzt fließt das Wasser wieder!"
}, {
    "open1": {
        "question": "Kannst du der Sache auf den Grund gehen? (ja/nein)",
        "ja": "Gehe nach Norden und schau dich da mal um. quest_start",
        "nein": "Okay schade, vielleicht ja später!"
    },
    "active2": { 
        "question": "Du erhälst dafür eine kleine Belohnung von mir, hoffe du kannst damit was anfangen (danke/nö)",
        "danke": "Kein Problem, danke dir! quest_done",
        "nö": "Okay, dann behalte ichs eben"
    }
})

inge = NPC("Inge", 100, 5, quest2, {
    "open": { # previous quest is active(ready) or not (blocked)
        "ready": "Durch den Damm den ich gebaut habe, sind die Fische endlich sicher und ich kann mich gut um sie kümmern.",
        "blocked": "Hier ist eine Frau die Fische füttert"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "",
        "blocked": "Besorge ein Aquarium um die Fische zu retten"
    },
    "done": "Der Wasserfall geht ja ganz schön tief!"
}, {
    "open1": {
        "question": "A: Der Wasserfall ist aber total ausgetrocknet!\nB: Darf ich auch mal Füttern?\nC: Okay, dann viel Spaß noch.",
        "a": "Ich würde dir ja gerne helfen, aber die Fische brauchen einen Ort zum Leben. Wenn es doch nur irgendwie einen weg geben würde, ein Aquarium zu besorgen... quest_start",
        "b": "*Fütter*",
        "c": "Danke"
    },
    "active2": { 
        "question": "Vielen Dank für das Aquarium! (kein problem/bitte schön, war ganz schön aufwendig)",
        "kein problem": "Super, jetzt kann ich die fische bei mir zuhause versorgen. quest_done",
        "bitte schön, war ganz schön aufwendig": "Oh, das tut mir leid quest_done"
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
        "ready": "Das hier muss der Vogel sein der weggeflogen ist...",
        "blocked": "Schöner Wald hier :)"
    },
    "active": { # next quest is done(ready) or not (blocked)
        "ready": "Dann versuche ich noch einmal den Vogel einzufangen!"
    },
    "done": "Dem Vogel geht es jetzt bestimmt besser!"
}, {
    "open1": {
        "question": "Na dann versuchen wir mal dich einzufangen (lets go)",
        "lets go": "Aber wie fange ich den Vogel am besten? quest_start"
    },
    "open2": {
        "question": "A: Vogelgeräusche imitieren \nB: Warten bis der Vogel weiter runter fliegt und ihn dann fangen \nC: Auf den Baum klettern und ihn fangen",
        "a": "Der Vogel denkt du bist ein Angreifer, du stirbst...",
        "b": "Glükwunssch du hast in gefangen quest_done",
        "c": "Du bist vom Baum gefallen und gestorben, lol"
    },
    "active3": {
        "question": "A: Vogelgeräusche imitieren \nB: Warten bis der Vogel weiter runter fliegt und ihn dann fangen \nC: Auf den Baum klettern und ihn fangen",
        "a": "Der Vogel denkt du bist ein Angreifer, du stirbst...",
        "b": "Glükwunssch du hast in gefangen quest_done",
        "c": "Du bist vom Baum gefallen und gestorben, lol"
    }
})

def get_dependencies(quests):
    dependencies = {}

    for i, quest in enumerate(quests):
        if i == 0:
            dependencies[quest.name] = "ready"
        else:
            dependencies[quest.name] = "ready" if quests[i - 1].state.name == "active" else "blocked"

    for i in range(len(quests) - 1):
        dependencies[f"{quests[i].name}_done"] = "ready" if quests[i + 1].state.name == "done" else "blocked"

    dependencies[f"{quests[-1].name}_done"] = "ready"

    return dependencies

def loadquests():
    for load_quest in save_and_load.load()["quests"]:
        for quest in quests:
            if load_quest.strip() == quest.name.strip():
                new_state_name = save_and_load.load()["quests"][load_quest]
                old_state_name = quest.state.name
                for state in quest.state_manager.states:
                    if state.name == new_state_name:
                        quest.state = state
