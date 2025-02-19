from state_quest import state_quest


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

class NPC (Person):
    def __init__(self, name, lives, strength, drop, quest: state_quest, dialogues: dict, choices: dict):
        self.quest = quest
        self.drop = drop
        self.dialogues = dialogues
        self.choices = choices
        super().__init__(lives, strength, name)

    def printInfo(self):
        super().printInfo()

    def talk(self, dependencies):
        print(dependencies.get(self.quest.name))
        print(dependencies.get(self.quest.name + "_done"))

        if self.quest.state == "open":
            print(f"\n{self.name}: {self.dialogues.get(self.quest.state)}")

            answer = input(">").lower().strip()

            response = self.choices[self.quest.state][answer]
            print(f"{self.name}: {response}")
            return

        elif self.quest.state == "active":
            print(f"{self.name}: {self.dialogues[self.quest.state][dependencies.get(self.quest.name + "_done")]}")
            return

        elif self.quest.state == "done":
            print(f"\n{self.name}: {self.dialogues.get(self.quest.state)}")
