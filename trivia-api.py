import json
import requests
import random

API_URL = "https://opentdb.com/api.php?amount=50"

response = requests.get(API_URL)
data = json.loads(response.text)
questions = data["results"]
points = 0

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
