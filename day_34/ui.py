from tkinter import *
from day_34.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0")
        self.score.config(fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30, padx=2)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="KE KE",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"))

        true = PhotoImage(file="images/true.png")
        self.b_right = Button(image=true, highlightthickness=0, command=self.button_true)
        self.b_right.config(padx=20, pady=20)
        self.b_right.grid(column=0, row=2)

        false = PhotoImage(file="images/false.png")
        self.b_false = Button(image=false, highlightthickness=0, command=self.button_false)
        self.b_false.config(padx=20, pady=20)
        self.b_false.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="END of the quiz")
            self.b_false.config(state="disabled")
            self.b_right.config(state="disabled")

    def button_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
        # self.get_next_question()

    def button_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
