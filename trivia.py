import json, random, time, threading
from rich import print as rprint

class Trivia:
  
    def quiz(quizFinished):

        with open("trivia.de.json", "r") as f:
            data = json.load(f)

        points = 0

        questions = data["results"]

        for question in questions:
            if quizFinished.is_set():
                break
            print(question["question"])
            print("Options:")
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
                    rprint("[green]richtiig[/green]")
                    points += 1
                else:
                    rprint(f"[red] {userInput} ist falsch.[/red] Die richtige Antwort wäre: " + question['correct_answer'])

            rprint(f"Du hast {points} von {len(questions)} möglichen Fragen richtig!\n")

    def timer(quizFinished):
        for i in range(30, 0, -1):
            if i % 5 == 0:
                rprint(f"\n[bright_magenta]Verbleibende Zeit: {i} Sekunden[/bright_magenta]")
            time.sleep(1)
        rprint("[red]Die zeit ist abgelaufen, mache deine letzte Eingabe...[/red]")
        quizFinished.set()

    def main(self):
        quizFinished = threading.Event()
        countdownThread = threading.Thread(target=self.timer, args=(quizFinished,))
        countdownThread.start()
        self.quiz(quizFinished)
        countdownThread.join()