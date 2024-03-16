import json
import random

with open("trivia.de.json", "r") as f:
    data = json.load(f)

points = 0

questions = data["results"]
for question in questions:
    print(question["question"])
    print("Options:")
    answers = []

    for i in range(len(question["incorrect_answers"])):
        answers.append(question["incorrect_answers"][i])

    random.randint(0,len(question["incorrect_answers"]))
    answers.insert(random.randint(0, len(question["incorrect_answers"])), question['correct_answer'])

    for i in range(len(answers)):
        print(f"{i+1}. {answers[i]}")

    userInput = input("Welche Antwort ist richtig? (Nur Zahlen erlaubt) \n>")

    if (int(userInput) == answers.index(question['correct_answer'])+1):
        print("yaaay")
        points += 1
    else:
        print("Die richtige Antwort wäre: " + question['correct_answer'])

    print(f"Du hast {points} von {len(questions)} möglichen Fragen richtig!\n")
