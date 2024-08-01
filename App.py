class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        for question, (options, correct_option) in self.questions.items():
            print("\n" + question)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            answer = int(input("Enter the correct option number: "))
            if options[answer - 1] == correct_option:
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        print(f"\nYour final score is {self.score}/{len(self.questions)}")

questions = {
    "What is the capital of France?": (["Berlin", "Madrid", "Paris", "Lisbon"], "Paris"),
    "Which planet is known as the Red Planet?": (["Earth", "Mars", "Jupiter", "Saturn"], "Mars"),
    "Who wrote 'To Kill a Mockingbird'?": (["Harper Lee", "Jane Austen", "J.K. Rowling", "Ernest Hemingway"], "Harper Lee")
}

quiz = Quiz(questions)
quiz.start()
