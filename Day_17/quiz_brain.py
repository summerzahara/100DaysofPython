class QuizBrain:
    def __init__(self, question_list):
        self.number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.number]
        self.number += 1
        user_response = input(f"Q.{self.number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_response, current_question.answer)

    def still_has_questions(self):
        count = len(self.question_list)
        return self.number < count

    def check_answer(self, response, answer):
        if response.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("WRONG!")
        print(f"The correct answer was {answer}")
        print(f"Your current score is: {self.score}/{self.number}")
        print("\n")
