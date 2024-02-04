
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            score += 1
    print(f"You got {score} out of {len(questions)} correct.")

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Questions for the quiz
question_prompts = [
    "1. Who was the first President of the United States?\n(a) Abraham 
Lincoln\n(b) George Washington\n(c) Thomas Jefferson\n\nAnswer: ",
    "2. In which year did the World War II begin?\n(a) 1939\n(b) 1941\n(c) 
1945\n\nAnswer: ",
    "3. Which empire was ruled by Genghis Khan?\n(a) Ottoman Empire\n(b) 
Mongol Empire\n(c) Roman Empire\n\nAnswer: ",
]

# Correct answers for the questions
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
]

run_quiz(questions)

