import time
class Notes:
     
    def read(self):
        note = open('introduction.txt', 'r')
        print(note.read())
        note.close()
    
    def write(self, text):
        note = open('introduction.txt', 'a')
        note.write("\n" + text)
        note.close()

    def delete(self, text):
        with open('introduction.txt', 'r') as fr:
            lines = fr.readlines()

            with open('introduction.txt', 'w') as fw:
                for line in lines:
                    if line.strip('\n') != text:
                        fw.write(line)
    def countdown():
        t = input("Enter the time in seconds: ")
        t = float(t)
        t = t*1000
        while t:
            sec, milisec = divmod(t, 1000)
            milisec = milisec / 10
            timer = f'{sec:.0f}:{milisec:.0f}'
            print(timer, end="\r")
            time.sleep(0.01)
            t -= 10
        print("Zeit ist abgelaufen!")       
