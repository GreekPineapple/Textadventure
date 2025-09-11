import random
from fight.enemy import Enemy

class Wizard(Enemy):
    name = "Magier"
    lives = 135
    strength = 40
    drop = "wizard überreste"
    active_effects = []
    blocked = False

    def apply_effect(self, effect):
        self.active_effects.append(effect)
        
    def remove_effect(self, effect):
        self.active_effects.remove(effect)

    def attack(self, player):
        if random.random() < 0.25:
            print("Der Magier schwächt dich mit einem Zauber")
            player.strength -= 5
        super().attack(player)

    def print_info(self):
        super().print_info()