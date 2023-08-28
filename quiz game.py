import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Your answer: ").strip().lower()
            self.check_answer(user_answer, question["answer"])
        self.display_final_score()

    def display_question(self, question):
        print(question["question"])
        if "options" in question:
            for i, option in enumerate(question["options"], start=1):
                print(f"{i}. {option}")
        print()

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    def display_final_score(self):
        print("Quiz completed!")
        print(f"Your score: {self.score} out of {len(self.questions)}")

# Sample questions for the quiz
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci"
    }
    # Add more questions here
]

if __name__ == "__main__":
    game = QuizGame(quiz_questions)
    print("Welcome to the Quiz Game!")
    print("Test your knowledge with these questions.\n")
    game.run()
