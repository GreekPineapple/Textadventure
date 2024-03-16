import json
import random

with open("trivia.json", "r") as f:
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

    userInput = input("What's the correct answer? (Numbers only) \n>")

    if (int(userInput) == answers.index(question['correct_answer'])+1):
        print("yaaay")
        points += 1
    else:
        print("schade")

    print(f"You got {points} out of {len(questions)} questions correct.")
