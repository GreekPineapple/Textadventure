from fight.attack import Attack

class Strength(Attack):
    name = "Stärke"
    price = 6
    type = "Potion"
    info = "   Vorteil: Verdoppelten deinen 2. Angriff\n   Nachteil: Nützt nur als erster Angriff was"

    def __init__(self, counter, name=None, price=None, type=None, info=None):
        super().__init__(counter, name, price, type, info)

    def make_damage(self, enemy):
        if self.counter > 0:
            self.counter -= 1
            return super().make_damage(self,enemy)
        else:
            return "\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n"
        
    
    def use_effect(self, enemy):
        pass