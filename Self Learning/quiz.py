# Self Learning Quiz Program
# This program asks questions, checks answers, and tracks score

def start_quiz():
    score = 0

    print("=== Welcome to Self Learning Quiz ===\n")

    questions = [
        {
            "question": "What is the output of 2**3?",
            "answer": "8"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "answer": "def"
        },
        {
            "question": "What is the data type of [1, 2, 3]?",
            "answer": "list"
        },
        {
            "question": "What does len('Hello') return?",
            "answer": "5"
        },
        {
            "question": "Which loop is used when the number of iterations is unknown?",
            "answer": "while"
        }
    ]

    for q in questions:
        print(q["question"])
        user_ans = input("Your answer: ").strip().lower()

        if user_ans == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")

    print("=== Quiz Finished ===")
    print(f"Your Score: {score}/{len(questions)}")

    if score == len(questions):
        print("Excellent! You're strong in basics.")
    elif score >= 3:
        print("Good, but improve more.")
    else:
        print("Weak basics. Practice more.")

# Run the program
start_quiz()