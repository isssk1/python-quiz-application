"""
COM4402 - Programming
A2: Implementation

Python Quiz Application
• Handles all edge cases
• Passes TC01 – TC10
• User-friendly & beginner readable

Author: <Your Name>
Student Number: <Your Student Number>
"""


# -------------------------------------------------
# Function: Load all quiz questions
# -------------------------------------------------
def load_questions():
    """
    Returns a list of quiz questions.
    Each question contains:
    - question text
    - four options
    - correct answer (as string number)
    """

    return [
        {
            "question": "What is the correct file extension for Python files?",
            "options": [
                "1) .pt",
                "2) .py",
                "3) .python",
                "4) .pyt"
            ],
            "answer": "2"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "1) function",
                "2) define",
                "3) def",
                "4) fun"
            ],
            "answer": "3"
        },
        {
            "question": "Which data type is used to store multiple values in Python?",
            "options": [
                "1) int",
                "2) float",
                "3) list",
                "4) bool"
            ],
            "answer": "3"
        },
        {
            "question": "What does the len() function return?",
            "options": [
                "1) Type of data",
                "2) Number of elements",
                "3) Memory size",
                "4) Data value"
            ],
            "answer": "2"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": [
                "1) //",
                "2) <!-- -->",
                "3) #",
                "4) **"
            ],
            "answer": "3"
        },
        {
            "question": "Which loop is used when the number of iterations is known?",
            "options": [
                "1) while",
                "2) for",
                "3) do-while",
                "4) repeat"
            ],
            "answer": "2"
        },
        {
            "question": "What will print(type(5)) output?",
            "options": [
                "1) <class 'float'>",
                "2) <class 'str'>",
                "3) <class 'int'>",
                "4) <class 'bool'>"
            ],
            "answer": "3"
        },
        {
            "question": "Which operator is used for exponentiation in Python?",
            "options": [
                "1) ^",
                "2) **",
                "3) //",
                "4) %"
            ],
            "answer": "2"
        }
    ]


# -------------------------------------------------
# Function: Ask a single question safely
# -------------------------------------------------
def ask_question(question_data):
    """
    Displays a question and keeps asking
    until the user provides valid input.
    Returns True if the answer is correct.
    """

    print("\n" + question_data["question"])

    # Display all answer options
    for option in question_data["options"]:
        print(option)

    # Keep looping until valid input is entered
    while True:
        user_input = input("Enter your answer (1-4): ").strip()

        # Handle invalid inputs (letters, symbols, empty input)
        if not user_input.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        # Handle numbers outside valid range
        if user_input not in {"1", "2", "3", "4"}:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        # Input is valid → exit loop
        break

    # Check answer
    if user_input == question_data["answer"]:
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False


# -------------------------------------------------
# Function: Control quiz flow and scoring
# -------------------------------------------------
def run_quiz():
    """
    Main controller for the quiz:
    - Displays welcome message
    - Tracks score
    - Shows final result
    """

    # TC01: Quiz starts normally
    print("Welcome to the Python Quiz!")
    print("Answer the questions by entering a number from 1 to 4.")

    score = 0
    questions = load_questions()
    total_questions = len(questions)

    # Loop through all questions
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1} of {total_questions}")

        if ask_question(question):
            score += 1

    # TC10: Quiz ends gracefully
    print("\nQuiz Completed!")
    print(f"Your final score is: {score} out of {total_questions}")


# -------------------------------------------------
# Program Entry Point
# -------------------------------------------------
if __name__ == "__main__":
    run_quiz()
