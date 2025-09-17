from fight.attack import Attack

class Strength(Attack):
    name = "Stärke"
    price = 6
    type = "Potion"
    info = "   Vorteil: Erhöt deine Stärke um 5\n   Nachteil: Betrifft nur deine reine kick stärke, ohne Waffen"

    def __init__(self, counter, name=None, price=None, type=None, info=None):
        super().__init__(counter, name, price, type, info)

    def make_damage(self, enemy, player):
        if self.counter > 0:
            player.strength += 5
            self.counter -= 1
            return super().make_damage(enemy)
        else:
            print("\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n")
            return 0
        
    
    def use_effect(self, enemy):
        pass