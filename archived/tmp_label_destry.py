from tkinter import *
import time

root =Tk()

label = Label(root, text="Text on the screen", font=('Times New Roman',  '80'), fg="black", bg="white")
label.pack()
time.sleep(1000)

#label.destroy()

root.mainloop()