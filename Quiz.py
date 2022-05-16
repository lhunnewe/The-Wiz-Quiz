import tkinter as tk
import os
class quiz:
    """in tKinter, quiz the user based upo csv files"""

    def __init__(self, quizzes=[]):
        """Initilaize"""
        self.quizzes = quizzes
    def file_scan(self):
        for quiz in os.listdir('.\\quizzes\\'):
            if quiz.endswith('.csv'):
                self.quizzes.append(quiz)
        print(self.quizzes)
Q = quiz()
Q.file_scan()