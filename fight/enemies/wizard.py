import random
from fight.enemy import Enemy

class Wizard(Enemy):
    name = "Magier"
    lives = 135
    strength = 35
    drop = "wizard überreste"
    active_effects = []
    blocked = False

    def apply_effect(self, effect):
        self.active_effects.append(effect)
        
    def remove_effect(self, effect):
        self.active_effects.remove(effect)

    def attack(self, player, fight_inventory):
        if random.random() < 0.25:
            print("Der Magier schwächt dich mit einem Zauber")
            player.strength -= 5
        super().attack(player, fight_inventory)

    def print_info(self):
        super().print_info()