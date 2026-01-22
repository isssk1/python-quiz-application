"""
COM4402 - Programming
A2: Implementation

Python Quiz Application
• Handles all edge cases
• Passes TC01 – TC10
• User-friendly & beginner readable

Author: Issa Khan
Number: 2421170
"""

def load_questions():
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


def ask_question(question_data):
    print("\n" + question_data["question"])


    for option in question_data["options"]:                   # Display all answer options
        print(option)

 
    while True:
        user_input = input("Enter your answer (1-4): ").strip()                 # Keep looping until valid input is entered


        if not user_input.isdigit():                                                                 # Handle invalid inputs (letters, symbols, empty input)
            print("Invalid input. Please enter a number between 1 and 4.")
            continue


        if user_input not in {"1", "2", "3", "4"}:                                                                    # Handle numbers outside valid range
            print("Invalid input. Please enter a number between 1 and 4.")
            continue


        break                                                                                                                         # Input is valid → exit loop

   
    if user_input == question_data["answer"]:
        print("Correct!")                                                                                                                            # Check answer
        return True
    else:
        print("Incorrect.")
        return False


def run_quiz():

    print("Welcome to the Python Quiz!")
    print("Answer the questions by entering a number from 1 to 4.")                           # TC01: Quiz starts normally

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

if __name__ == "__main__":
    run_quiz()
