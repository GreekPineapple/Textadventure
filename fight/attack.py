import csv

class Attack:
    def __init__(self,counter=None, name=None, price=None, type=None, info=None):
        self.counter = counter if counter is not None else getattr(self, "counter", None)
        self.name = name if name is not None else getattr(self, "name", None)
        self.price = price if price is not None else getattr(self, "price", None)
        self.type = type if type is not None else getattr(self, "type", None)
        self.info = info if info is not None else getattr(self, "info", None)

    def use_effect(self, enemy):
        pass

    def make_damage(self, enemy):
        with open('fight/damage_table.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter=',')
            for row in reader:
                if row['Weapon'] == self.name:
                    return int(row[enemy.name])