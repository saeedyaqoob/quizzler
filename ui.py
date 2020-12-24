from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label = Label()
        self.label.config(bg=THEME_COLOR, fg="white", font=("Courier", 10, "normal"))
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=250, height=300)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(125, 150, width=250, fill="black", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.button_true = Button(image=true_image, borderwidth=0, highlightthickness=0, command=self.answer_true)
        self.button_true.grid(column=0, row=2)

        self.button_false = Button(image=false_image, borderwidth=0, highlightthickness=0, command=self.answer_false)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.canvas.itemconfig(
                self.question_text,
                text=f"The Quiz has ended.\n\n"
                f"Total questions: {self.quiz.question_number}\n\n"
                f"Correctly answered: {self.quiz.score}\n\n"
                f"Wrongly answered: {self.quiz.question_number - self.quiz.score}")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
