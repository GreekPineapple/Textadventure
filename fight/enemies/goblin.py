import random
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
        if random.random() < 0.3 and player.inventory.items:
            stolen_item = random.choice(list(player.inventory.items))
            print(f"Der Goblin klaut dir '{stolen_item}' aus deinem Inventar!")
            player.inventory.remove(stolen_item)
        super().attack(player)

    def print_info(self):
        super().print_info()