#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import random
import subprocess
import unittest

def ask_question():
    questions = {
        "What is the capital of France?": "Paris",
        "Which planet is known as the Red Planet?": "Mars",
        "What is the largest mammal in the world?": "Blue Whale",
        "In which year did the Titanic sink?": "1912",
        "How many continents are there?": "7"
    }

    question = random.choice(list(questions.keys()))
    correct_answer = questions[question]

    print("\nQuestion: " + question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == correct_answer.lower():
        print("Correct! Well done.")
        return True
    else:
        print("Incorrect. The correct answer is: " + correct_answer)
        return False

def quiz_game():
    print("Welcome to the Quiz Game!\n")
    score = 0
    num_questions = 5

    for _ in range(num_questions):
        if ask_question():
            score += 1

    print("\nQuiz completed!")
    print("Your final score is:", score, "out of", num_questions)

class TestQuizGame(unittest.TestCase):
    def test_ask_question(self):
        # Implement your test cases for ask_question function here
        pass

    # You can add more test cases for other functions if needed

def initialize_git():
    # Specify the full path to the Git executable
    git_executable_path = r"C:/Users/User/Downloads/Git-2.43.0-64-bit.exe"

    # Initialize Git repository
    subprocess.run([git_executable_path, "init"])
    print("Git repository initialized.")

    # Create a .gitignore file to exclude unnecessary files
    with open(".gitignore", "w") as gitignore:
        gitignore.write("__pycache__/\n*.pyc\n")
    print(".gitignore created.")

    # Stage and commit the initial files
    subprocess.run([git_executable_path, "add", "."])
    subprocess.run([git_executable_path, "commit", "-m", "Initial commit"])
    print("Initial commit done.")

def build():
    # Nothing specific to build for now
    print("Build successful.")

if __name__ == "__main__":
    # Create a test suite and add the TestQuizGame class to it
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuizGame)

    # Run the tests
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Initialize Git
    initialize_git()

    # Perform build
    build()
    print("Build successful.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




