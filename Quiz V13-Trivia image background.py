from tkinter import *
import os
import random
import tkinter


root=Tk()  #tkinteer root file
root.geometry("800x600")  #tkinter appication lend and width
root.title("The Wiz Quiz")  #Screen bar title

class menu:
    """This class creates a opening menu to select a quiz and passes the selected quiz to the Quiz class"""
    def __init__(self):
        """To create a menu to select a Quiz"""
        self.quizzes = []
        self.file_scan()
        
        height = 800 #Height of the canvas
        width = 600 #Width of the canvas
        canvas = Canvas(root,height=height,width=width) #Declaring the height/width of canvas
        canvas.pack() #Packing the canvas

        self.bg_image = PhotoImage(file='bg01.png')  #Declaring variable as image location
        bg_label = Label(root,image=self.bg_image)  #Assigning image to a label that is mapped to the root
        bg_label.place(relwid=1,relheight=1)  #Placing the label to 100% of the canvas

        self.frame_hdr = Frame(root,bg='gray',bd=5)  #Creating a Frame for the header
        self.frame_hdr.place(relx=0.0,rely=0.01,relwidth=1.0,relheight=0.1)  #Placement of Frame, xy are defaulted to NW of the grid

        label_hdr=Label(self.frame_hdr,text='The Wiz Quiz',font=('Times',18))  #Label that goes inside the header with Text
        label_hdr.place(relx=0.00,rely=0,relwidth=1.0,relheight=0.95)  #xy and relative width and height to the frame
        
        self.frame_p=Frame(root,bg='gray',bd=5)  #Main frame to apply the Listbox onto
        self.frame_p.place(relx=0.25,rely=0.25,relwidth=0.50,relheight=.55)

        self.pf_listbox = Listbox(self.frame_p) #Listbox for showing the list of project files
        for i, p in enumerate(self.quizzes):  #inserts the list of quizzes into the listbox
            self.pf_listbox.insert(i,p)
        self.pf_listbox.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=.90)  #placees the listbox

        button_submit=Button(self.frame_p,font=('courier',10),text='Select Quiz',relief= 'groove', command=self.quiz_select)  #Selcts the quiz and passes it to class Quiz
        button_submit.place(relx=0.0,rely=0.90,relwidth=1.0,relheight=0.10)

    def file_scan(self):
        """To scan all the csv files in folder quizzes so the end user can select which quiz they would like to do"""
        for quiz in os.listdir('.\\quizzes\\'):
            if quiz.endswith('.csv'):
                self.quizzes.append(quiz)
    def quiz_select(self):
        """Stores the selected quiz and assigns the bg_image to the quiz. Passes the selected quiz to the class Quiz to run"""
        for i in self.pf_listbox.curselection():
            print(self.pf_listbox.get(i))
            quiz_sel = self.pf_listbox.get(i)
        fname = quiz_sel[:-4]
        # print(fname)
        try:
            # self.bg_image = PhotoImage(file='.\\quizzes\\' + fname + '.png') #Declaring variable as image location
            self.bg_image = PhotoImage(file='bg01.png')
        except:
            self.bg_image = PhotoImage(file='bg01.png')
        bg_label = Label(root,image=self.bg_image) #Assigning image to a label that is mapped to the root
        bg_label.place(relwid=1,relheight=1) #Placing the label to 100% of the canvas
        self.frame_p.destroy()
        self.frame_hdr.destroy()
        Q = quiz(active_quiz=quiz_sel)        

class quiz:
    """class quiz quizzes the user based upon the selected csv file from class menu"""

    def __init__(self, active_quiz):
        """Loops through the selected csv quiz until there are no more questions or until the user ends the quiz early"""
        
        self.frame_result=Frame(root,bd=5, highlightbackground="black", highlightthickness=2, bg="gray")  #Displays the results of quiz such as correct answers, wrong answers and correct %
        self.frame_result.place(relx=0.13,rely=0.15,relwidth=0.75,relheight=.35)
        label_hdr=Label(self.frame_result,text='The Wiz Quiz Results',font=('Times',18))  #Label that goes inside the header with Text
        label_hdr.place(relx=0.00,rely=0.0,relwidth=1.0,relheight=0.15)  #xy and relative width and height to the frame
        
        self.frame_p=Frame(root,bd=5, highlightbackground="black", highlightthickness=2, bg="gray")  #frame_p is the primary quiz frame for displaying the question and possible answers
        self.frame_p.place(relx=0.13,rely=0.15,relwidth=0.75,relheight=.35)
        
        self.frame_b=Frame(root,bd=5, highlightbackground="black", highlightthickness=2, bg="gray")  #frame_b is the bottom frame for the next and end quiz button
        self.frame_b.place(relx=0.13,rely=0.75,relwidth=0.75,relheight=.10)

        self.active_quiz = active_quiz  #The selected quiz that was passed from class menu
        self.questions = []  #list of all the questions answers and possible answers
        self.quiz_open(self.active_quiz)  #Method to open the selected quiz from class menu
        self.opt_selected = IntVar()  #allows to get/set the variable
        self.opts = self.radiobtns()  #Display the four radio buttons
        
        self.q_number = 1  #the active question number. This is used to index from list questions and display on the screen
        self.ques = self.question(self.q_number)  #Calls method to assign and display the question to the Label
        self.display_options(self.q_number)
        self.buttons()
        self.correct=0
    def question(self, q_number):
        """Assigns the next increemental question to the Label"""
        q_number = Label(self.frame_p, text=self.questions[q_number][0], width=45, font=("times", 16, "bold"), anchor="w", bg="gray")
        q_number.place(x=0, y=10)
        return q_number
    def radiobtns(self):
        """Creates the four radio buttons for the user to select"""
        val = 0
        B = []
        yp = 50
        while val < 4:
            btn = Radiobutton(self.frame_p, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14),bg="gray",activebackground="gray")
            B.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 25
        return B
    def display_options(self, q_number):
        """Displays the active question and possible answers"""
        val = 0
        self.opt_selected.set(0)  #sets the radio buttons
        self.ques['text'] = self.questions[q_number][0]  #Calls method question to update the question Label
        choices = self.questions[q_number][2]  #parse the possible answers
        for choice in choices[0]:
            self.opts[val]['text'] = choice  #assign each radio button a choice/possible answer
            val +=1
    def buttons(self):
        """Assigns the next and quit button to frame_b"""
        nbutton = Button(self.frame_b, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.pack(side=tkinter.RIGHT)
        quitbutton = Button(self.frame_b, text="End Quiz", command=self.display_result,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.pack(side=tkinter.LEFT)
    
    def checkans(self, q_number):
        """To compare the selected answer with the from the csv file"""
        ans = self.questions[q_number][1]  #get the answer to the active question
        choices = self.questions[q_number][2]  
        selected_ans = choices[0][self.opt_selected.get()-1]  #rretrieves the selected answer from thhe radio buttons
        if ans == selected_ans:
            num_questions = len(self.questions) -1
            print(selected_ans, 'is correct.', 'correct answers: ',self.correct +1,'out of', num_questions)
            return True
    def nextbtn(self):
        """To call check answer and to display the next question"""
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
        """To raise/display the end game frame results"""
        self.frame_b.destroy()
        self.buttons_results()
        # num_question = len(self.questions) -1
        if self.q_number != 1:
            num_question = self.q_number -1
        else:
            num_question = self.q_number
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
        """To add the quit button to the display results frame"""
        quitbutton = Button(self.frame_result, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.pack(side=tkinter.BOTTOM)


M = menu()
root.mainloop()

