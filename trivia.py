import json, random, time, threading
from rich import print as rprint

class Trivia:
  
    def quiz(quizFinished):

        with open("trivia.de.json", "r") as f:
            data = json.load(f)

        points = 0

        questions = data["results"]

        for question in sorted(questions,key=lambda _: random.random()):
            if quizFinished.is_set():
                break
            print(question["question"])
            answers = []

            for i in range(len(question["incorrect_answers"])):
                answers.append(question["incorrect_answers"][i])

            random_index = random.randint(0,len(question["incorrect_answers"]))
            answers.insert(random_index, question['correct_answer'])

            for i in range(len(answers)):
                print(f"{i+1}. {answers[i]}")

            userInput = input("Welche Antwort ist richtig? (Nur Zahlen erlaubt) \n>")

            try:
                int(userInput)
            except:
                rprint(f"[red]Antwort '{userInput}' nicht gefunden[/red]")
            else:
                if (int(userInput) == answers.index(question['correct_answer'])+1):
                    rprint(f"[green]{userInput} ist richtig[/green]")
                    points += 1
                else:
                    rprint(f"[red]{userInput} ist falsch.[/red] Die richtige Antwort wäre: " + question['correct_answer'])

            rprint(f"Du hast {points} von {len(questions)} möglichen Fragen richtig!\n")

        return points

    def timer(quizFinished):
        for i in range(100, 0, -1):
            if i % 5 == 0:
                rprint(f"\n[bright_magenta]Verbleibende Zeit: {i} Sekunden[/bright_magenta]")
            time.sleep(1)
        rprint("[red]Die zeit ist abgelaufen, mache deine letzte Eingabe...[/red]")
        quizFinished.set()

    def main(self, player):
        quizFinished = threading.Event()
        countdownThread = threading.Thread(target=self.timer, args=(quizFinished,))
        countdownThread.start()
        points = self.quiz(quizFinished)
        countdownThread.join()
        if points >= 10:
            print("Glückwunsch, du hast den Geheimweg freigeschalten :)")
            time.sleep(2)
            print(" .", end="\r")
            time.sleep(1)
            print(" ..", end="\r")
            time.sleep(1)
            print(" ...")
            time.sleep(2)
            print("Auf dem Weg findest du eine Kiste deren Inhalt du mitnimmst..")
            time.sleep(1)
            # weiteres Bauteil geben
            player.inventory["Bauteil2"] += 1
            player.secretPath = True
            return True
        else:
            print("Leider hast du den Test nicht bestanden :(")