import time
import threading
import queue

class BossWithThread:
    def __init__(self, name):
        self.name = name
        self.player_inputs = queue.Queue()
        self.running = True

    def bossAction(self):
        while self.running:
            try:
                user_input = self.player_inputs.get(timeout=3)
            except queue.Empty:
                print("Boss macht was er will!")
                continue

            if user_input == "1":
                print("Boss-Reaktion auf Input 1: Angriff!")
            elif user_input == "5":
                print("Boss-Reaktion auf Input 5: Verteidigung!")
            elif user_input == "stop":
                self.running = False
                print("Boss stoppt den Kampf.")
            else:
                print(f"Boss versteht '{user_input}' nicht.")

            time.sleep(0.5)
    
    def playerAction(self):
        print("Mach was: (z.B. 1, 5, stop)")
        while self.running:
            user_input = input().strip()
            self.player_inputs.put(user_input)
            if user_input == "stop":
                print("Spieler hat gestoppt!")
                break
            print("Mach was:")


if __name__ == "__main__":
    game = BossWithThread("Endboss")
    thread = threading.Thread(target=game.bossAction)
    thread2 = threading.Thread(target=game.playerAction)
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()