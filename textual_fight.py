import threading
from typing import Container
from textual.app import App, ComposeResult, on
from textual.widgets import Static, Input
from textual.containers import Container

class FormApp(App):
    def compose(self) -> ComposeResult:
        yield Container(
            Static("Blah bli blub", id="player"),
            Static("Dupdidupdidup", id="villain"),
            id="first_row"
        )
        yield Input(placeholder="Input here", type="text", id="input_field")

    def on_mount(self) -> None:
        self.screen.styles.layout = "vertical"
        
        self.widget1 = self.query_one("#player")
        self.widget1.styles.width = "50%"
        self.widget1.styles.height = "100%"
        self.widget1.border_title = "Player"
        self.widget1.styles.border = ("heavy", "blue")
        self.widget1.styles.padding = (1,3)
        
        self.widget2 = self.query_one("#villain")
        self.widget2.styles.width = "50%"
        self.widget2.styles.height = "100%"
        self.widget2.border_title = "Villain"
        self.widget2.styles.border = ("heavy", "yellow")
        self.widget2.styles.padding = (1,3)
        
        first_row = self.query_one("#first_row")
        first_row.styles.layout = "horizontal"
        first_row.styles.height = "70%"
        
        self.widget3 = self.query_one("#input_field")
        self.widget3.styles.width = "100%"
        self.widget3.styles.height = "30%"
        self.widget3.styles.border = ("heavy", "green")
        self.widget3.styles.padding = (1,3)
        
        self.stop = threading.Event()
        self.villainThread = threading.Thread(target=self.villain_action, args=())
        self.villainThread.start()
   
    def villain_action(self):
        while not self.stop.is_set():
            self.call_from_thread(self.widget2.update, "Whoooo Ich bin der Geist")
            if self.stop.wait(1): break
            
            self.call_from_thread(self.widget2.update, "Ich gehe bis in deinen Raum")
            if self.stop.wait(1): break
            
        self.call_from_thread(self.widget2.update, "Boooo")
        
    @on(Input.Submitted)
    def player_action(self, event: Input.Submitted):
        text = event.value
        self.widget1.update(text)
        self.widget3.value = ""
        
        if text == "stop":
            self.stop.set()
    
if __name__ == "__main__":
    FormApp().run()
    