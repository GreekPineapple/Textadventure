import time

def countdown(t, callback):
    t = t*1000
    while t:
        sec, milisec = divmod(t, 1000)
        milisec = milisec / 10
        timer = f"{sec:.0f}:{milisec:.0f}"
        callback(timer)
        time.sleep(0.01)
        t -= 10
    callback("Zeit ist abgelaufen!")
