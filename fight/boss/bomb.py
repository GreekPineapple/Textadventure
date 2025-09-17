class Bomb:
    name = "Bombe"
    price = 8
    type = "Mehrfachangriff"
    damage = 60
    counter = 2

    def make_damage(self, enemy, player):
        if self.counter > 0:
            self.counter -= 1
            return self.damage
        else:
            print("Die Bombe kann nicht mehr verwendet werden.")
            return 0