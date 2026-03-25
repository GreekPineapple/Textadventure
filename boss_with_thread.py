import json, random, time, threading

class BossWithThread:
    def __init__(self, name):
        self.name = name

    def bossAction():
        while True:
            print("Boss macht was er will!")
            time.sleep(3)
    
    def playerAction():
        print("Mach was:") 
        while input() != "stop":
            print("Mach was:")
        print("Spieler hat gestoppt!")

    if __name__ == "__main__":
        thread = threading.Thread(target=bossAction)
        thread2 = threading.Thread(target=playerAction)
        thread.start()
        thread2.start()