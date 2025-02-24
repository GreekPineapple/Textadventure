class state_quest:
    def __init__(self, name, start_desc, complete_desc, note):
        self.state = "open"  # Startzustand
        self.name = name
        self.start_desc = start_desc
        self.complete_desc = complete_desc
        self.note = note
        
    def start(self):
        if self.state == "open":
            self.state = "active"
            print(f"Quest '{self.name}' gestartet!")
            self.note.write(self.start_desc)

    def complete(self):
        if self.state == "active":
            self.state = "done"
            print(f"Quest '{self.name}' abgeschlossen!")
