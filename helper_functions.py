# Author: Dikla Buchnik
# Function: ask_question(player)
# Part of Quiz Quest Project
import random
def ask_question(player, questions, score):
    category = input(f"{player}, choose a category: science, history, pop culture: ").lower()
 #if he choose an invalid category:
    if category not in questions:
        print("error: invalid category, moving to the next player")
        return
#if he choose a valid category:
    question_data = random.choice(questions[category])
#printing the question from the category:
    print(question_data["q"])
#asking for answer from the player
    answer = input("Enter your answer: ").lower()
    if answer == question_data["a"].lower():
        print("Correct!")
        scores[player] += 1
        print(f"{player}'s score is {scores[player]}")
    else:
        print(f"Wrong answer! The correct answer is {question_data['a']}")


   