import time

def countdown(t, quizFinished):
    t = t*1000
    while t:
        sec, milisec = divmod(t, 1000)
        milisec = milisec / 10
        timer = f"{sec:.0f}:{milisec:.0f}"
        print(timer, end="\r")
        time.sleep(0.01)
        t -= 10
    print("Zeit ist abgelaufen!") 
    quizFinished.set()