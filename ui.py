from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
# SCORE=0


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", foreground="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.questionText = self.canvas.create_text(
            150, 125,width=280, text="This is my Question Text, which i always want", fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0,command=self.false_press)
        self.false_btn.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}", foreground="White", bg=THEME_COLOR)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=q_text)
        else:
            self.canvas.itemconfig(self.questionText,text= "You've reached to the end of the quiz")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    
    def true_press(self):
        # print('True is pressed')
        self.give_feedback(self.quiz.check_answer('True'))
        # self.get_next_question()
        


    def false_press(self):
        # print('false is pressed')
        self.give_feedback(self.quiz.check_answer('False'))
        # self.get_next_question()


    
    def give_feedback(self, answer):
        if answer==True:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)
        


    