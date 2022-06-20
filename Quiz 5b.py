from tkinter import *
import os
import random

root=Tk()
root.geometry("800x500")
root.title("The Wiz Quiz")


class quiz:
    """In tKinter, quiz the user based upon the selected csv file"""

    def __init__(self, quizzes=[], questions=[], stats=[]):
        """Initialize"""
        self.active_quiz = 'A Presidential Dinner.csv' #active_quiz
        self.questions = questions
        self.quiz_open(self.active_quiz)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.q_number = 1
        self.ques = self.question(self.q_number)
        self.display_options(self.q_number)
        self.buttons()
        self.correct=0
        
        self.quizzes = quizzes
        self.stats = []
    def question(self, q_number):
        quiz_name= self.active_quiz[:-4]  #excludes csv extension in header
        t = Label(root, text=quiz_name, width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=self.questions[q_number][0], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn
    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b
    def display_options(self, q_number):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = self.questions[q_number][0]
        choices = self.questions[q_number][2]
        for choice in choices[0]:
            self.opts[val]['text'] = choice
            val +=1
    def buttons(self):
        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.place(x=380,y=380)
    
    def checkans(self, q_number):
        #print('Questions: ', self.questions[q_number], 'selected: ',self.opt_selected.get())
        ans = self.questions[q_number][1]
        choices = self.questions[q_number][2]
        selected_ans = choices[0][self.opt_selected.get()-1]
        if ans == selected_ans:
            print(selected_ans, 'is correct.', 'correct answers: ',self.correct +1)
            return True
        
    def nextbtn(self):
        if self.checkans(self.q_number):
            self.correct += 1
        self.q_number += 1
        if self.q_number == len(self.questions):
            self.display_result()
        else:
            self.display_options(self.q_number)   
    def file_scan(self):
        """To scan all the csv files in folder quizzes so the end user can select which quiz they would like to do"""
        for quiz in os.listdir('.\\quizzes\\'):
            if quiz.endswith('.csv'):
                self.quizzes.append(quiz)
    def quiz_select(self):
        """Allows the end user to select which quiz they would like to do"""
        for i, quiz in enumerate(self.quizzes):
            print('Select a quiz by number(0-99): ')
            print(i, quiz)
            ans = input('Quiz: ')
            #quiz_select = self.quizzes[int(ans)]
            self.active_quiz = self.quizzes[int(ans)]
            #return quiz_select
    def quiz_open(self, quiz):
        """To generate and randomize the list of questions"""
        with open('.\\quizzes\\' + quiz) as f:
            #f.readline()
            for line in f:
                line = line.rstrip('\n')
                index, q, ans, p1,p2,p3 = line.split(',')
                choices = [ans,p1,p2,p3]
                random.shuffle(choices)
                self.questions.append([q,ans,[choices]])


Q = quiz()
root.mainloop()

