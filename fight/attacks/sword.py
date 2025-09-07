from fight.attack import Attack

class Sword(Attack):
    name = "Schwert"
    price = 4
    type = "Attack"
    info = "   Vorteil: Dein Angriff in der nächsten Runde ist um 5 Punkte stärker \n   Nachteil: Unwirksam bei Gegnern die fliegen"
    counter = 0

    def make_damage(self, enemy):
        enemy.apply_effect(self)
        self.counter = 2
        return super().make_damage(self,enemy)
    
    def use_effect(self, enemy):
        print("enemy.lives before effect:", enemy.lives)
        if self.counter == 1:
            enemy.lives -= 5
            print("enemy.lives after effect:", enemy.lives)
            enemy.remove_effect(self)
        self.counter -= 1