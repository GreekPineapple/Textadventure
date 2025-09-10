import json,globals
class SaveAndLoad:
 
    def save(self, position, inventory, lives, armor, quess_dict):
        snapshot = {
            "position": position,
            "inventory": inventory,
            "lives": lives,
            "armor": armor,
            "quests": quess_dict 
        }
        with open("checkpoint.json", "w") as f:
            json.dump(snapshot, f)

    def load(self):
        with open("checkpoint.json", "r") as f:
            snapshot = json.load(f)
            return snapshot
