import random
from fight.enemy import Enemy

class Goblin(Enemy):
    name = "Goblin"
    lives = 90
    strength = 30
    drop = "goblin überreste"
    active_effects = []
    blocked = False

    def apply_effect(self, effect):
        self.active_effects.append(effect)
        
    def remove_effect(self, effect):
        self.active_effects.remove(effect)

    def attack(self, player, fight_inventory):
        if random.random() < 0.3 and fight_inventory.items:
            stolen_item = random.choice(list(fight_inventory.items))
            if not stolen_item == "kick":
                print(f"Der Goblin klaut dir '{stolen_item}' aus deinem Inventar!")
                fight_inventory.remove(stolen_item)
        super().attack(player, fight_inventory)

    def print_info(self):
        super().print_info()