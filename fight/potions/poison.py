from fight.attack import Attack

class Poison(Attack):
    name = "Gift"
    price = 6
    type = "Potion"
    info = "   Vorteil: Gegner macht in der nächsten Runde keinen Schaden an dir\n   Nachteil: Nur leichter schaden in der aktuellen Runde"
        
    def make_damage(self, enemy):
        enemy.apply_effect(self)
        return super().make_damage(self,enemy)