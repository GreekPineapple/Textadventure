from fight.attack import Attack

class Sword(Attack):
    name = "Schwert"
    price = 4
    type = "Attack"
    info = "   Vorteil: Dein Angriff in der nächsten Runde ist um 5 Punkte stärker \n   Nachteil: Unwirksam bei Gegnern die fliegen"
    counter_next_round = 0

    def __init__(self, counter, name=None, price=None, type=None, info=None):
        super().__init__(counter, name, price, type, info)

    def make_damage(self, enemy, player):
        if self.counter > 0:
            self.counter -= 1
            enemy.apply_effect(self)
            self.counter_next_round = 2
            return super().make_damage(enemy)
        else:
            print("\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n")
            return 0
    
    def use_effect(self, enemy):
        if self.counter_next_round == 1:
            enemy.lives -= 5
            enemy.remove_effect(self)
        self.counter_next_round -= 1