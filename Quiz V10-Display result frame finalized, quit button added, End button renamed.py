from tkinter import *
import os
import random
import tkinter


root=Tk()
root.geometry("800x500")
root.title("The Wiz Quiz")

class menu:
    def __init__(self):
        """To create a menu to select a Quiz"""
        self.quizzes = []
        self.file_scan()
        
        height = 600 #Height of the canvas
        width = 600 #Width of the canvas
        canvas = Canvas(root,height=height,width=width) #Declaring the height/width of canvas
        canvas.pack() #Packing the canvas

        self.bg_image = PhotoImage(file='bg01.png') #Declaring variable as image location
        #bg_image = PhotoImage(file='bg01.png') #Declaring variable as image location
        bg_label = Label(root,image=self.bg_image) #Assigning image to a label that is mapped to the root
        bg_label.place(relwid=1,relheight=1) #Placing the label to 100% of the canvas

        self.frame_hdr = Frame(root,bg='gray',bd=5) #Creating a Frame for the header
        self.frame_hdr.place(relx=0.0,rely=0.01,relwidth=1.0,relheight=0.1) #Placement of Frame, xy are defaulted to NW of the grid

        label_hdr=Label(self.frame_hdr,text='The Wiz Quiz',font=('Times',18))#Label that goes inside the header with Text
        label_hdr.place(relx=0.00,rely=0,relwidth=1.0,relheight=0.95)#xy and relative width and height to the frame
        
        #frame_p
        self.frame_p=Frame(root,bg='gray',bd=5)
        self.frame_p.place(relx=0.25,rely=0.15,relwidth=0.50,relheight=.55)

        #global pf_listbox 
        self.pf_listbox = Listbox(self.frame_p) #Listbox for showing the list of project files
        for i, p in enumerate(self.quizzes):
            self.pf_listbox.insert(i,p)
        #pf_listbox.bind('<<ListboxSelect>>',self.CurSelect())#Upon clicking, stores selected value RESEARCH THIS!
        self.pf_listbox.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=.90)

        button_submit=Button(self.frame_p,font=('courier',10),text='Select Quiz',relief= 'groove', command=self.quiz_select)
        button_submit.place(relx=0.0,rely=0.90,relwidth=1.0,relheight=0.10)

    def file_scan(self):
        """To scan all the csv files in folder quizzes so the end user can select which quiz they would like to do"""
        for quiz in os.listdir('.\\quizzes\\'):
            if quiz.endswith('.csv'):
                self.quizzes.append(quiz)
    def quiz_select(self):
        for i in self.pf_listbox.curselection():
            print(self.pf_listbox.get(i))
            quiz_sel = self.pf_listbox.get(i)
        fname = quiz_sel[:-4]
        print(fname)
        self.bg_image = PhotoImage(file='.\\quizzes\\' + fname + '.png') #Declaring variable as image location
        bg_label = Label(root,image=self.bg_image) #Assigning image to a label that is mapped to the root
        bg_label.place(relwid=1,relheight=1) #Placing the label to 100% of the canvas
        self.frame_p.destroy()
        self.frame_hdr.destroy()
        Q = quiz(active_quiz=quiz_sel)        

class quiz:
    """In tKinter, quiz the user based upon the selected csv file"""

    def __init__(self, active_quiz):
        """Initialize"""
        
        self.frame_result=Frame(root,bd=5) #How to hide frames???
        self.frame_result.place(relx=0.05,rely=0.05,relwidth=0.90,relheight=.35)
        label_hdr=Label(self.frame_result,text='The Wiz Quiz Results',font=('Times',18))  #Label that goes inside the header with Text
        label_hdr.place(relx=0.00,rely=0,relwidth=1.0,relheight=0.15)  #xy and relative width and height to the frame
        
        self.frame_p=Frame(root,bd=5)
        self.frame_p.place(relx=0.05,rely=0.05,relwidth=0.90,relheight=.35)
        
        self.frame_b=Frame(root,bd=5)
        self.frame_b.place(relx=0.05,rely=0.75,relwidth=0.90,relheight=.10)

        self.active_quiz = active_quiz
        self.questions = []
        self.quiz_open(self.active_quiz)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.q_number = 1
        self.ques = self.question(self.q_number)
        self.display_options(self.q_number)
        self.buttons()
        self.correct=0
        # height = 500 #Height of the canvas
        # width = 600 #Width of the canvas
        # canvas = Canvas(root,height=height,width=width) #Declaring the height/width of canvas
        # canvas.pack() #Packing the canvas 
    def question(self, q_number):
        #quiz_name= self.active_quiz[:-4]  #excludes csv extension in header
        #t = Label(root, text=quiz_name, width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        #t.place(x=0, y=2)
        #qn = Label(root, text=self.questions[q_number][0], width=60, font=("times", 16, "bold"), anchor="w")
        q_number = Label(self.frame_p, text=self.questions[q_number][0], width=60, font=("times", 16, "bold"), anchor="w")
        q_number.place(x=70, y=10)
        return q_number
    def radiobtns(self):
        val = 0
        B = []
        yp = 50
        while val < 4:
            #btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            btn = Radiobutton(self.frame_p, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            B.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 25
        return B
    def display_options(self, q_number):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = self.questions[q_number][0]
        choices = self.questions[q_number][2]
        for choice in choices[0]:
            self.opts[val]['text'] = choice
            val +=1
    def buttons(self):
        nbutton = Button(self.frame_b, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.pack(side=tkinter.RIGHT)
        quitbutton = Button(self.frame_b, text="End Quiz", command=self.display_result,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.pack(side=tkinter.LEFT)
    
    def checkans(self, q_number):
        #print('Questions: ', self.questions[q_number], 'selected: ',self.opt_selected.get())
        ans = self.questions[q_number][1]
        choices = self.questions[q_number][2]
        selected_ans = choices[0][self.opt_selected.get()-1]
        if ans == selected_ans:
            num_questions = len(self.questions) -1
            print(selected_ans, 'is correct.', 'correct answers: ',self.correct +1,'out of', num_questions)
            return True
    def nextbtn(self):
        if self.checkans(self.q_number):
            self.correct += 1
        self.q_number += 1
        if self.q_number == len(self.questions):
            self.display_result()
        else:
            self.display_options(self.q_number)
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
    def display_result(self):
        self.frame_b.destroy()
        self.buttons_results()
        # num_question = len(self.questions) -1
        num_question = self.q_number -1
        score = int(self.correct / num_question * 100)
        result = "Score: " + str(score) + "%"
        wc = num_question - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        
        self.frame_result.tkraise()
        l_correct = Label(self.frame_result, text=correct)
        l_correct.place(relx=0.25,rely=0.3,relwidth=.5,relheight=0.10)

        l_wrong = Label(self.frame_result, text=wrong)
        l_wrong.place(relx=0.25,rely=0.4,relwidth=.5,relheight=0.10)

        l_score = Label(self.frame_result, text=result)
        l_score.place(relx=0.25,rely=0.5,relwidth=.5,relheight=0.10)
    def buttons_results(self):
        quitbutton = Button(self.frame_result, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.pack(side=tkinter.BOTTOM)


M = menu()
root.mainloop()

