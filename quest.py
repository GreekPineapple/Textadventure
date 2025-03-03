class Quest:
    def __init__(self, name, start_desc, complete_desc, note, state_manager, prev_quest=None):
        self.state = state_manager.states[0] #"open"  # Startzustand
        self.name = name
        self.start_desc = start_desc
        self.complete_desc = complete_desc
        self.note = note
        self.prev_quest = prev_quest
        self.next_quest = None
        self.state_manager = state_manager

        if prev_quest:
            prev_quest.next_quest = self
        
    def start(self):
        if self.state.__class__ == self.state_manager.states[0].__class__:
            self.state = self.state.update()
            # print(f"Quest '{self.name}' gestartet!")
            if self.prev_quest:
                self.note.delete(self.prev_quest.start_desc)
            self.note.write(self.start_desc)

    def complete(self):
        if self.state.__class__ == self.state_manager.states[1].__class__:
            self.state = self.state.update()
            #print(f"Quest '{self.name}' abgeschlossen!")
            if self.next_quest:
                self.note.delete(self.next_quest.complete_desc)
            else:
                self.note.delete(self.start_desc)
            self.note.write(self.complete_desc)
