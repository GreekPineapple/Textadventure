from fight.attack import Attack

class SharpRain(Attack):
    name = "Scharfer Regen"
    price = 4
    type = "Attack"
    info = "   Vorteil: Greift mehrere Gegner gleichzeitig an \n   Nachteil: Meist nicht so stark"
    
    def __init__(self, counter, name=None, price=None, type=None, info=None):
        super().__init__(name, price, type, info)
        self.counter = counter

    def make_damage(self, enemy):
        if self.counter > 0:
            self.counter -= 1
            return super().make_damage(self,enemy)
        else:
            return "\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n"
    