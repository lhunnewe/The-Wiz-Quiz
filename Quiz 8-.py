from tkinter import *
import os
import random
from tkinter import messagebox


root=Tk()
root.geometry("800x500")
root.title("The Wiz Quiz")

class menu:
    def __init__(self):
        """To create a menu to select a Quiz"""
        self.quizzes = []
        self.file_scan()
        
        height = 500 #Height of the canvas
        width = 600 #Width of the canvas
        canvas = Canvas(root,height=height,width=width) #Declaring the height/width of canvas
        canvas.pack() #Packing the canvas

        self.bg_image = PhotoImage(file='bg01.png') #Declaring variable as image location
        #bg_image = PhotoImage(file='bg01.png') #Declaring variable as image location
        bg_label = Label(root,image=self.bg_image) #Assigning image to a label that is mapped to the root
        bg_label.place(relwid=1,relheight=1) #Placing the label to 100% of the canvas

        frame_hdr = Frame(root,bg='gray',bd=5) #Creating a Frame for the header
        frame_hdr.place(relx=0.0,rely=0.01,relwidth=1.0,relheight=0.1) #Placement of Frame, xy are defaulted to NW of the grid

        label_hdr=Label(frame_hdr,text='The Wiz Quiz',font=('Times',18))#Label that goes inside the header with Text
        label_hdr.place(relx=0.00,rely=0,relwidth=1.0,relheight=0.95)#xy and relative width and height to the frame
        
        #frame_p
        self.frame_p=Frame(root,bg='gray',bd=5)
        self.frame_p.place(relx=0.05,rely=0.15,relwidth=0.90,relheight=.75)

        #global pf_listbox 
        self.pf_listbox = Listbox(self.frame_p) #Listbox for showing the list of project files
        for i, p in enumerate(self.quizzes):
            self.pf_listbox.insert(i,p)
        #pf_listbox.bind('<<ListboxSelect>>',self.CurSelect())#Upon clicking, stores selected value RESEARCH THIS!
        self.pf_listbox.place(relx=0,rely=0.15,relwidth=1.0,relheight=1.0)

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
        Q = quiz(active_quiz=quiz_sel)        

class quiz:
    """In tKinter, quiz the user based upon the selected csv file"""

    def __init__(self, active_quiz):
        """Initialize"""
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
        
        #self.quizzes = []
        #self.stats = []

        height = 500 #Height of the canvas
        width = 600 #Width of the canvas
        canvas = Canvas(root,height=height,width=width) #Declaring the height/width of canvas
        canvas.pack() #Packing the canvas
    def question(self, q_number):
        #quiz_name= self.active_quiz[:-4]  #excludes csv extension in header
        #t = Label(root, text=quiz_name, width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        #t.place(x=0, y=2)
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
            print(selected_ans, 'is correct.', 'correct answers: ',self.correct +1,'out of', len(self.questions))
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
        score = int(self.correct / len(self.questions) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(self.questions) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        messagebox.showinfo("Result", "\n".join([result, correct, wrong]))


M = menu()
root.mainloop()

