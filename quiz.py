import random
import time

easy_questions = [
    {
        "Question": "What is the capital  of France?",
        "Options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"], 
        "Answer": "A"
    }, 
    {
        "Question": "What is the capital  of India?",
        "Options": ["A. Bengaluru", "B. Mumbai", "C. Chennai", "D. Delhi"], 
        "Answer": "D"
    },
    {
        "Question": "What is the capital  of USA?",
        "Options": ["A. New York", "B. Washington DC", "C. Miami", "D. Florida"], 
        "Answer": "B"
    }
]

medium_questions = [
    {
        "Question": "Which Gas do plants absorb from the Air?",
        "Options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Helium"], 
        "Answer": "B"
    },
    {
        "Question": "Who invented the telephone?",
        "Options": ["A. Steve Jobs", "B. Einstein", "C. Newton", "D. Alexander Graham Bell"], 
        "Answer": "D"
    },
    {
        "Question": "What is the colour of Sun?",
        "Options": ["A. Black", "B. Blue", "C. White", "D. Red"], 
        "Answer": "C"
    }
]

hard_questions = [
    {
        "Question": "What is Square Root of 256?",
        "Options": ["A. 14", "B. 16", "C. 18", "D. 20"], 
        "Answer": "B"
    },
    {
        "Question": "Which year was python first released?",
        "Options": ["A. 1989", "B. 1991", "C. 1995", "D. 2000"], 
        "Answer": "B"
    }
]

# quiz = random.sample(questions, 3)

level = input("Choose difficulty Level (Easy/Medium/Hard): ").strip().lower()
if level == "easy":
    selected_questions = easy_questions
elif level == "medium":
    selected_questions = medium_questions
elif level == "hard":
    selected_questions = hard_questions
else:
    print("Invalid level selected. Defaulting to medium.")
    selected_questions = medium_questions

quiz = random.sample(selected_questions, min(2, len(selected_questions)))

Score = 0
print("Welcome to the Quiz Game!\n")
print(f"Difficulty Level:{level.capitalize()}\n")
for i, q in enumerate(quiz, 1):
    print(f"Q{i}: {q["Question"]}")
    for Options in q ["Options"]:
        print(Options)

    start = time.time()
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    end = time.time()

    if end - start > 10:
        print("Time's Up! No point awarded.\n")
        continue

    if user_answer == q["Answer"]:
        print("Correct!\n")
        Score += 1
    else:
        print(f"Incorrect! Correct Answer is {q['Answer']}\n ")

print(f"Your Final Score: {Score} out of {len(quiz)}")
print(f"Percentage: {(Score/len(quiz)) * 100: .2f}%")
print(f"You took {end - start: .2f} seconds.\n")
