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
    def __init__(self, name, lives, strength, quest, drop):
        self.quest = quest
        self.drop = drop
        super().__init__(lives, strength, name)

    def printInfo(self):
        super().printInfo()

    def szeneOpen(self):
        print("Hier ist das Gespräch wenn die quest noch nicht aktiv ist") 
    
    def szeneActive(self):
        print("Hier ist das Gespräch wenn die quest aktiv ist")
    
    def szeneDone(self):
        print("Hier ist das Gespräch wenn die quest erledigt ist")
