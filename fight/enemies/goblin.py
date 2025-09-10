from fight.enemy import Enemy

class Goblin(Enemy):
    name = "Goblin"
    lives = 90
    strength = 35
    drop = "goblin überreste"
    active_effects = []
    blocked = False

    def apply_effect(self, effect):
        self.active_effects.append(effect)
        
    def remove_effect(self, effect):
        self.active_effects.remove(effect)

    def attack(self, player):
        super().attack(player)  
