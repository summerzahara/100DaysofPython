from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        # self.score.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0, borderwidth=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Super import question.",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(column=1, columnspan=2, row=2, pady=50)

        self.true_img = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=self.true_img, highlightthickness=0, borderwidth=0, command=self.true_check)
        self.button_true.grid(column=1, row=3)

        self.false_img = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=self.false_img, highlightthickness=0, borderwidth=0, command=self.false_check)
        self.button_false.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_check(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)
        return result

    def false_check(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)
        return result

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
