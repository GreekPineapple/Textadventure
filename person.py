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
        print(self.quest.name)
        print(dependencies.get(self.quest.name))
        print(dependencies.get(self.quest.name + "_done"))

        if self.quest.state == "open":
            print(f"\n{self.name}: {self.dialogues[self.quest.state][dependencies.get(self.quest.name)]}")

        elif self.quest.state == "active":
            print(f"{self.name}: {self.dialogues[self.quest.state][dependencies.get(self.quest.name + "_done")]}")

        elif self.quest.state == "done":
            print(f"\n{self.name}: {self.dialogues.get(self.quest.state)}")

        for index, key in enumerate(self.choices):
            swi = self.quest.state + str(index + 1) #State with Index (swi)
            if key == swi:
                print(self.choices[swi]["question"])
                answer = input(">").lower().strip()
                response = self.choices[swi][answer]
                print(f"{self.name}: {response}")