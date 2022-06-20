from tkinter import *
import os
import random

class quiz:
    """In tKinter, quiz the user based upon csv files"""

    def __init__(self, quizzes=[], questions=[], stats=[]):
        """Initilaize"""
        self.quizzes = quizzes
        self.questions = questions
        self.stats = []
    def start(self):
        self.file_scan()
        quiz = self.quiz_select()
        print('quiz selected: ', quiz)
        self.quiz_open(quiz)
        for question in range(1,len(self.questions)):
            q = self.get_question(question)
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
            quiz_select = self.quizzes[int(ans)]
            return quiz_select
    def quiz_open(self, quiz):
        """To generate and randomize the list of questions"""
        with open('.\\quizzes\\' + quiz) as f:
            #f.readline()
            for line in f:
                line = line.rstrip('\n')
                index, q, ans, p1,p2,p3 = line.split(',')
                answers = [ans,p1,p2,p3]
                random.shuffle(answers)
                self.questions.append([index,q,ans,[answers]])
    def get_question(self, question_num):
        """To get the active question"""
        question = self.questions[question_num]
        print(question)
        return question

Q = quiz()
Q.start()

