class Square:
    def explore(self):
        pass

class TownHall:
    def start(self):
        intro = open('introduction.txt', 'r')
        print(intro.read())
        
    def explore(self):
        print("Wuhuu")
class Waterfall:
    def explore(self):
        print('Rainer: "Oh man, hier war mal ein schöner Wasserfall, aber irgenjemand musste ja unbedingt ein Staudamm in Richtung Norden bauen...')
        print('Kannst du der Sache auf den Grund gehen? (yes / no)"')
        option = input(">")
        if option.lower() == "yes":
            pass
        elif option.lower() == "no":
            print('Rainer: "Okay schade, vielleicht ja später!"')
        else:
            print("ungültige eingabe")
class Dam:
    def explore(self):
        pass

class Aquarium:
    def explore(self):
        pass

class BirdHouse:
    def explore(self):
        pass

class Woods:
    def explore(self, player):
        player.inventory.append("potion")
        print(player.inventory)

class SouthWoods:
    def explore(self):
        pass

class WestWoods:
    def explore(self):
        pass

class EastWoods:
    def explore(self):
        pass