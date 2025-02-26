class state_quest:
    def __init__(self, name, start_desc, complete_desc, note, prev_quest=None):
        self.state = "open"  # Startzustand
        self.name = name
        self.start_desc = start_desc
        self.complete_desc = complete_desc
        self.note = note
        self.prev_quest = prev_quest
        self.next_quest = None

        if prev_quest:
            prev_quest.next_quest = self
        
    def start(self):
        if self.state == "open":
            self.state = "active"
            print(f"Quest '{self.name}' gestartet!")
            if self.prev_quest:
                self.note.delete(self.prev_quest.start_desc)
            self.note.write(self.start_desc)

    def complete(self):
        if self.state == "active":
            self.state = "done"
            print(f"Quest '{self.name}' abgeschlossen!")

            if self.next_quest:
                self.note.delete(self.next_quest.complete_desc)
            else:
                self.note.delete(self.start_desc)
            self.note.write(self.complete_desc)
