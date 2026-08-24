import threading
from typing import Container
from textual.app import App, ComposeResult, on
from textual.widgets import Label, ProgressBar, Static, Input
from textual.containers import Container
from textual.message import Message

class FormApp(App):
    
    class VillainAttack(Message):
        pass
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("Wähle einen Angriff", id="player"),
            Container(
                Label("Dauer bis Gegner angreift: "),
                ProgressBar(total=100, show_eta=False, id="progress_bar"),
                Static("", id="villain"),
                id="villain_container"
            ), 
            id="first_row"
        )
        yield Input(placeholder="Input here", type="text", id="input_field")

    def on_mount(self) -> None:
        self.screen.styles.layout = "vertical"
        
        self.playerText = self.query_one("#player")
        self.playerText.styles.width = "50%"
        self.playerText.styles.height = "100%"
        self.playerText.border_title = "Player"
        self.playerText.styles.border = ("heavy", "blue")
        self.playerText.styles.padding = (1,3)
        
        self.villainText = self.query_one("#villain")
        self.villainText.styles.width = "100%"
        self.villainText.styles.margin = (2,0,0,0)
        
        self.villainContainer = self.query_one("#villain_container")
        self.villainContainer.styles.layout = "vertical"
        self.villainContainer.styles.width = "50%"
        self.villainContainer.border_title = "Villain"
        self.villainContainer.styles.border = ("heavy", "yellow")
        self.villainContainer.styles.padding = (1,3)
        
        self.progressBar = self.query_one("#progress_bar")
        self.progressBar.styles.width = "100%"
        
        first_row = self.query_one("#first_row")
        first_row.styles.layout = "horizontal"
        first_row.styles.height = "70%"
        
        self.inputBox = self.query_one("#input_field")
        self.inputBox.styles.width = "100%"
        self.inputBox.styles.height = "30%"
        self.inputBox.styles.border = ("heavy", "green")
        self.inputBox.styles.padding = (1,3)
        
        self.player_attack = threading.Event()
        self.villainThread = threading.Thread(target=self.villain_action, args=())
        self.villainThread.start()
   
    def villain_action(self):
        x=0
        while True:
            x+=10
            self.call_from_thread(self.progressBar.update, progress=x)
            if self.player_attack.wait(1): 
                self.villainText.update("Gegner wurde angegriffen") 
                self.call_from_thread(self.progressBar.update, progress=0)
                self.player_attack.clear()
                x=0
            if self.progressBar.progress == self.progressBar.total:
                self.post_message(self.VillainAttack())
                x=0
            
    # Villain listens for Input
    @on(Input.Submitted)
    def player_action(self, event: Input.Submitted):
        text = event.value
        self.playerText.update(text)
        self.inputBox.value = ""
        
        if text == "angriff":
            self.player_attack.set()
        
    #Player listens to VillainAttack, a Message postet after progressbar is on 100%
    @on(VillainAttack)
    def handle_villain_attack(self):
        self.playerText.update("Du wurdest angegriffen")
           
if __name__ == "__main__":
    FormApp().run()
    