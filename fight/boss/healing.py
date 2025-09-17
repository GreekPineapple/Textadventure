class Healing:
    name = "heiltrank"
    price = 4
    type = "Trank"
    damage = 0
    counter = 1

    def make_damage(self, enemy, player):
        if self.counter > 0:
            player.lives = 250
            self.counter -= 1
        else:
            print("Du kannst den Heiltrank nur einmal benutzen!")  
        return self.damage
