from fight.attack import Attack

class SharpRain(Attack):
    name = "Scharfer Regen"
    price = 4
    type = "Attack"
    info = "   Vorteil: Greift mehrere Gegner gleichzeitig an \n   Nachteil: Meist nicht so stark"
    
    def make_damage(self, enemy):
        return super().make_damage(self,enemy)
    