class state_quest:
    def __init__(self, name, description):
        self.state = "open"  # Startzustand
        self.name = name
        self.description = description
        
    def start(self):
        if self.state == "open":
            self.state = "active"
            print(f"Quest '{self.name}' gestartet!")

    def complete(self):
        if self.state == "active":
            self.state = "done"
            print(f"Quest '{self.name}' abgeschlossen!")
