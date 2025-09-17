from fight.attack import Attack

class Poison(Attack):
    name = "Gift"
    price = 6
    type = "Potion"
    info = "   Vorteil: Gegner macht in der nächsten Runde keinen Schaden an dir\n   Nachteil: Nur leichter schaden in der aktuellen Runde"

    def __init__(self, counter, name=None, price=None, type=None, info=None):
        super().__init__(counter, name, price, type, info)
        
    def make_damage(self, enemy, player):
        if enemy.name == "Boss":
            enemy.paralize = True
            print("Der Boss ist jetzt für die nächste Runde gelähmt")
        else:
            if self.counter > 0:
                self.counter -= 1
                enemy.apply_effect(self)
                return super().make_damage(enemy)
            else:
                print("\nDu hast jetzt zu oft den selben angriff genutzt. Der Gegner lernt daraus und ist jetzt immun...\n")
                return 0
    
    def use_effect(self, enemy):
        if enemy.blocked:
            enemy.remove_effect(self)
            enemy.blocked = False
        else:
            enemy.lives -= 3
            enemy.blocked = True