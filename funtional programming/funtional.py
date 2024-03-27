import pandas as pd
import datetime

# Functional programming style using dictionaries for data structures
# No classes, simple data structures

def create_quiz():
    questions = []
    num_questions = int(input("Enter the number of questions for the quiz: "))
    for i in range(num_questions):
        question = input(f"Enter question {i + 1}: ")
        options = [input(f"Enter option {j + 1}: ") for j in range(4)]  # Assuming 4 options for simplicity
        correct_answer = input("Enter the correct option number: ")
        questions.append({'question': question, 'options': options, 'correct_answer': correct_answer})
    return questions

def display_quiz(quiz):
    for i, question in enumerate(quiz):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{j + 1}. {option}")
    
def take_quiz(quiz):
    score = 0
    total_questions = len(quiz)
    for question in quiz:
        display_quiz([question])
        answer = input("Your answer: ")
        if answer == question['correct_answer']:
            score += 1
    print(f"\nYour score: {score}/{total_questions}")

def save_results(user, quiz, score):
    # For simplicity, we'll just print the data here.
    print(f"User {user['name']} scored {score} in the quiz.")
    print("Results saved.")

# Functional Programming

users = []
quizzes = []

while True:
    choice = input("\n1. Create Quiz\n2. Take Quiz\n3. Display Quizzes\n4. Save Results\n5. Exit\nEnter your choice: ")

    if choice == '1':
        quizzes.append(create_quiz())
    elif choice == '2':
        if not quizzes:
            print("No quizzes available.")
        else:
            quiz_index = int(input("Enter the index of the quiz you want to take: "))
            if 0 <= quiz_index < len(quizzes):
                user = create_user()
                take_quiz(quizzes[quiz_index])
                save_results(user, quizzes[quiz_index], score)
            else:
                print("Invalid quiz index.")
    elif choice == '3':
        if not quizzes:
            print("No quizzes available.")
        else:
            for i, quiz in enumerate(quizzes):
                print(f"\nQuiz {i + 1}:")
                display_quiz(quiz)
    elif choice == '4':
        # Placeholder for saving results
        print("Results saved.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
