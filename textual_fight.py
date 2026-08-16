import time
from typing import Container

from textual.app import App, ComposeResult, on
from textual.widgets import Static, Input
from textual.containers import Container
import countdown, threading

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
        
        # self.countdownThread = threading.Thread(target=countdown.countdown, args=(5, self.update_countdown))
        # self.countdownThread.start()
        
        self.playerThread = threading.Thread(target=self.player_action, args=())
        self.playerThread.start()
        self.villainThread = threading.Thread(target=self.villain_action, args=())
        self.villainThread.start()
        
    # def update_countdown(self, timer):
    #     self.call_from_thread(self.widget2.update, timer)
        
        
    def villain_action(self):
        pass
        # self.call_from_thread(self.widget1.update, "Whoooo Ich bin der Geist")
        # time.sleep(2)
        # self.call_from_thread(self.widget1.update, "Ich gehe bis in deinen Raum")
        # time.sleep(2)
        # self.call_from_thread(self.widget1.update, "Boohoo")
        
    @on(Input.Submitted)
    def player_action(self):
        self.widget1.update(self.widget3.value)
        self.widget3.value = ""
       # self.call_from_thread(self.widget3.update, "input")
    
if __name__ == "__main__":
    FormApp().run()
    