from collections import Counter

class Inventory:

    def __init__(self, counter=None):
        self.items = Counter() if counter is None else counter

    def add(self, item, quantity=1):
        self.items[item] += quantity

    def remove(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def print_inventory(self):
        if not self.items:
            print("Dein Inventar ist leer.")
        else:
            print("Dein Inventar:")
            for item, quantity in self.items.items():
                print(f"{item:.<18}{quantity}")

    def has_item(self, item):
        return True  if self.items.get(item, 0) > 0 else False

    def get_item(self, item):
        return self.items.get(item, 0)