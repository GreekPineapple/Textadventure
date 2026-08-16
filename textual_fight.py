import time

from textual.app import App
from textual.widgets import Static
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
        self.widget1.border_title = "Player"
        self.widget1.styles.border = ("heavy", "blue")
        self.widget1.styles.padding = (1,3)
        
        self.widget2.styles.width = "50%"
        self.widget2.styles.height = "100%"
        self.widget2.border_title = "Villain"
        self.widget2.styles.border = ("heavy", "yellow")
        self.widget2.styles.padding = (1,3)
        
        self.countdownThread = threading.Thread(target=countdown.countdown, args=(5, self.update_countdown))
        self.countdownThread.start()
        
        self.villainThread = threading.Thread(target=self.villain_action, args=())
        self.villainThread.start()
        
    def update_countdown(self, timer):
        self.call_from_thread(self.widget2.update, timer)
        
        
    def villain_action(self):
        self.call_from_thread(self.widget1.update, "Whoooo Ich bin der Geist")
        time.sleep(2)
        self.call_from_thread(self.widget1.update, "Ich gehe bis in deinen Raum")
        time.sleep(2)
        self.call_from_thread(self.widget1.update, "Boohoo")
        
if __name__ == "__main__":
    FormApp().run()
    