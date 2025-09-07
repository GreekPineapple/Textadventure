from fight.attack import Attack

class Strength(Attack):
    name = "Stärke"
    price = 6
    type = "Potion"
    info = "   Vorteil: Verdoppelten deinen 2. Angriff\n   Nachteil: Nützt nur als erster Angriff was"

    def make_damage(self, enemy):
        return super().make_damage(self,enemy)