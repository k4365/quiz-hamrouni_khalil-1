# A historical quiz game in Python with enhanced features

class Question:
    def __init__(self, prompt, answer, difficulty):
        self.prompt = prompt
        self.answer = answer
        self.difficulty = difficulty

def ask_question(question):
    print(f"Difficulty: {question.difficulty}")
    answer = input(question.prompt + "\nAnswer: ")
    if answer.lower() == question.answer.lower():
        print("Correct!\n")
        return True
    else:
        print("Incorrect!")
        print(f"The correct answer was: {question.answer}\n")
        return False

def run_quiz(questions):
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    percentage = (score / len(questions)) * 100
    print(f"You got {score} out of {len(questions)} correct.")
    print(f"Your final score is: {percentage:.2f}%")

    # Ask the user if they want to retry the quiz
    retry = input("Would you like to try the quiz again? (yes/no): ").lower()
    if retry == "yes":
        run_quiz(questions)

# List of questions for the quiz
questions = [
    Question("Who was the first President of the United States?", "b", "Easy"),
    Question("In which year did the World War II begin?", "a", "Medium"),
    Question("Which empire was ruled by Genghis Khan?", "b", "Hard"),
]

# Question prompts
question_prompts = [
    "1. Who was the first President of the United States?\n(a) Abraham Lincoln\n(b) George 
Washington\n(c) Thomas Jefferson",
    "2. In which year did the World War II begin?\n(a) 1939\n(b) 1941\n(c) 1945",
    "3. Which empire was ruled by Genghis Khan?\n(a) Ottoman Empire\n(b) Mongol Empire\n(c) Roman 
Empire",
]

# Assign prompts to questions
for i, question in enumerate(questions):
    question.prompt = question_prompts[i]

# Run the quiz
run_quiz(questions)


