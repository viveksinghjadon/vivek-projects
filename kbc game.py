# List of questions and answers
questions = {
    1: {"question": "Who is the first Prime Minister of India?", "answer": "Jawaharlal Nehru"},
    2: {"question": "What is the capital of India?", "answer": "New Delhi"},
    3: {"question": "Who is the author of 'A Brief History of Time'?", "answer": "Stephen Hawking"},
    4: {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    5: {"question": "Who is the founder of Microsoft?", "answer": "Bill Gates"}
}

# Function to ask a question
def ask_question(question_number, score):
    question = questions[question_number]["question"]
    answer = questions[question_number]["answer"]

    print(f"Question {question_number}: {question}")
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}")

    return score

# Main game loop
score = 0
for i in range(1, 6):
    score = ask_question(i, score)
    print(f"Your current score is {score}")

print("Game over!")