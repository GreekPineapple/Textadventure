import random
import globals

class Enemy:
    
    def print_info (self):
        print(f"\nDu wirst vom {globals.COLOR_NOUN}{self.name}{globals.COLOR_RESET} angegriffen")
        print(f"Leben: {self.lives}")
        print(f"Stärke: {self.strength}\n" )

    def apply_effect(self, effect):
        self.active_effects.append(effect)
        
    def remove_effect(self, effect):
        self.active_effects.remove(effect)

    def attack(self, player, fight_inventory):

        if random.random() < 0.20:
            print(f"Der gegner macht einen {globals.COLOR_NOUN}Spezialangriff{globals.COLOR_RESET},")
            if fight_inventory.has_item("ausweichmanöver"):
                
                print(f"aber du weichst dem {globals.COLOR_NOUN}Spezialangriff{globals.COLOR_RESET} aus")
                fight_inventory.remove("ausweichmanöver")
            else:
                print("und du wirst getroffen")
                player.lives -= self.strength * 2 * player.armmor_points
            print(f"Deine verbleibenden Leben: {player.lives}\n")
        else:
            player.lives -= self.strength * player.armmor_points
            print(f"Deine verbleibenden Leben: {player.lives}\n")
    

        