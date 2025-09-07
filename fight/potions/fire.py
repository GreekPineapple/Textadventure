from fight.attack import Attack

class Fire(Attack):
    name = "Feuer"
    price = 6
    type = "Potion"
    info = "   Vorteil: Gegner nimmt 3 Runden zusätzlichen schaden\n   Nachteil: kann nur einmal benutzt werden"
 
    def make_damage(self, enemy):
        enemy.apply_effect(self)
        return super().make_damage(self,enemy)
                   