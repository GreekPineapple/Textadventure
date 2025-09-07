import random
from fight.attack import Attack

class Bow(Attack):
    name = "Bogen"
    price = 4
    type = "Attack"
    info = "   Vorteil: Der stärkste Angriff \n   Nachteil: Trefferwahrscheinlichkeit nur bei 90%"
    
    def make_damage(self, enemy):
        if random.random() < 0.10:
            print("Leider hast du daneben geschossen")
            return 0
        else:
            return super().make_damage(self,enemy)