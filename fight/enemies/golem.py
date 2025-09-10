from fight.enemy import Enemy

class Golem(Enemy):
    name = "Erdgolem"
    lives = 140
    strength = 50
    drop = "golem überreste"
    active_effects = []
    blocked = False

    def apply_effect(self, effect):
        self.active_effects.append(effect)
        
    def remove_effect(self, effect):
        self.active_effects.remove(effect)

    def attack(self, player):
        super().attack(player)

    def print_info(self):
        super().print_info()