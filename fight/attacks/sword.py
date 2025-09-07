from fight.attack import Attack

class Sword(Attack):
    name = "Schwert"
    price = 4
    type = "Attack"
    info = "   Vorteil: Der darauffolgende Angriff ist um 5 Punkte stärker \n   Nachteil: Unwirksam bei Gegnern die fliegen"
    
    def make_damage(self, enemy):
        return super().make_damage(self,enemy)
   