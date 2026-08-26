import threading
from textual.app import App, ComposeResult, on
from textual.widgets import Input
from textual.containers import Horizontal
from textual.message import Message
from player_container import PlayerContainer
from villain_container import VillainContainer

class FormApp(App):
    
    class VillainAttack(Message):
        pass

    CSS_PATH = "styles.tcss"
    
    def compose(self) -> ComposeResult:

        with Horizontal(id="first_row"):
            yield PlayerContainer(id="player_container")
            yield VillainContainer(id="villain_container")
        
        yield Input(placeholder="Input here", type="text", id="input_field")

    def on_mount(self) -> None:
        
        self.last_input = ""
        self.playerText = self.query_one("#player")
        self.villainText = self.query_one("#villain")
        self.villainContainer = self.query_one("#villain_container")
        self.playerContainer = self.query_one("#player_container")
        self.progressBar = self.query_one("#progress_bar")        
        self.inputBox = self.query_one("#input_field")
        self.villainContainer.border_title = "Villain"
        self.playerContainer.border_title =  "Player"
        self.lives = self.query(".live-sidebar")

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
        self.last_input = event.value
        self.playerText.update(self.last_input)
        self.inputBox.value = ""
        
        if self.last_input == "angriff":
            self.player_attack.set()
        
    #Player listens to VillainAttack, a Message postet after progressbar is on 100%
    @on(VillainAttack)
    def handle_villain_attack(self):
        if self.last_input == "abwehr":
            self.playerText.update("Du wurdest nicht angegriffen")
        else:
            self.playerText.update("Du wurdest angegriffen")
           
if __name__ == "__main__":
    FormApp().run()
    