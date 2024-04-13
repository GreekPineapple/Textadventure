import json, random, time, threading
from rich import print as rprint
from rich.progress import track

class Trivia:
  
    def quiz():#quizFinished):

        with open("trivia.de.json", "r") as f:
            data = json.load(f)

        points = 0

        questions = data["results"]

        for question in questions:
            # if quizFinished.is_set():
            #     break
            rprint(question["question"])
            rprint("Options:")
            answers = []

            for i in range(len(question["incorrect_answers"])):
                answers.append(question["incorrect_answers"][i])

            random_index = random.randint(0,len(question["incorrect_answers"]))
            answers.insert(random_index, question['correct_answer'])

            for i in range(len(answers)):
                rprint(f"{i+1}. {answers[i]}")

            userInput = input("Welche Antwort ist richtig? (Nur Zahlen erlaubt) \n>")

            try:
                int(userInput)
            except:
                rprint("Antwort '" + userInput + "' nicht gefunden")
            else:
                if (int(userInput) == answers.index(question['correct_answer'])+1):
                    rprint("yaaay")
                    points += 1
                else:
                    rprint("Die richtige Antwort wäre: " + question['correct_answer'])

            rprint(f"Du hast {points} von {len(questions)} möglichen Fragen richtig!\n")

    def quizTimer():#quizFinished):
        for i in track(range(20)):
            time.sleep(1)
       # quizFinished.set()

    quizFinished = threading.Event()
    countdownThread = threading.Thread(target=quizTimer)#, args=(quizFinished))
    countdownThread.start()
    quiz()#quizFinished)
    countdownThread.join()