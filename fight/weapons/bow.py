import random
from fight.attack import Attack

class Bow(Attack):
    name = "Bogen"
    price = 4
    type = "Attack"
    info = "   Vorteil: Der stärkste Angriff \n   Nachteil: Trefferwahrscheinlichkeit nur bei 90%"
    
    def __init__(self, counter, name=None, price=None, type=None, info=None):
        super().__init__(name, price, type, info)
        self.counter = counter

    def make_damage(self, enemy):
        if self.counter > 0:
            self.counter -= 1
            if random.random() < 0.10:
                print("Leider hast du daneben geschossen")
                return 0
            else:
                return super().make_damage(self,enemy)
        else:
            return "\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n"
       