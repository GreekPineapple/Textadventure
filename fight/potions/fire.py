from fight.attack import Attack

class Fire(Attack):
    name = "Feuer"
    price = 6
    type = "Potion"
    info = "   Vorteil: Gegner nimmt 3 Runden zusätzlichen schaden\n   Nachteil: kann nur einmal benutzt werden"
    used = False
    counter = 3
 
    def make_damage(self, enemy):
        enemy.apply_effect(self)
        return super().make_damage(self,enemy)
                   
    def use_effect(self, enemy):
        if self.used:
            print("Dieser Trank wurde schon benutzt und kann nur einmla benutzt werden")
        elif self.counter > 0:
            enemy.lives -= 8
            self.counter -= 1
        if self.counter == 0:
            enemy.remove_effect(self)
            self.used = True