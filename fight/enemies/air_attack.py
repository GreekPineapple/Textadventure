import random
from fight.enemy import Enemy

class AirEnemy(Enemy):
    name = "Luftgegner"
    lives = 110
    strength = 25
    drop = "vogel überreste"
    active_effects = []
    blocked = False

    def apply_effect(self, effect):
        self.active_effects.append(effect)
        
    def remove_effect(self, effect):
        self.active_effects.remove(effect)
        
    def attack(self, player, fight_inventory):
        print("Der Ggner wirft einen Gegenstand auf dich ")
        if random.random() < 0.5:
            print("aber du kannst ihm ausweichen")
        else:
            print("und du wirst getroffen")
            player.lives -= 3
        super().attack(player, fight_inventory)

    def print_info(self):
        super().print_info()