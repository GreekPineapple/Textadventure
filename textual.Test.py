from textual.app import App
from textual.widgets import Input, Label, Button, Digits, Placeholder, Static
from textual import on
import countdown, threading

class FormApp(App):
    def compose(self):
        self.widget1 = Static("Blah bli blub")
        yield self.widget1
        self.widget2 = Static("Dupdidupdidup")
        yield self.widget2

    def on_mount(self) -> None:
        self.screen.styles.layout = "horizontal"
        
        self.widget1.styles.width = "50%"
        self.widget1.styles.height = "100%"
        self.widget1.border_title = "Villain"
        self.widget1.styles.border = ("heavy", "yellow")
        self.widget1.styles.padding = (1,3)
        
        self.widget2.styles.width = "50%"
        self.widget2.styles.height = "100%"
        self.widget2.border_title = "Player"
        self.widget2.styles.border = ("heavy", "blue")
        self.widget2.styles.padding = (1,3)
        
        self.countdownThread = threading.Thread(target=countdown.countdown, args=(5, self.update_countdown))
        self.countdownThread.start()
        
        
    def update_countdown(self, timer):
        self.call_from_thread(self.widget2.update, timer)
        
if __name__ == "__main__":
    FormApp().run()
    