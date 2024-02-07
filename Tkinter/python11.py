import tkinter as tk
from tkinter import messagebox
def show_message():
    messagebox.showinfo("Info","This is an informational message.")
def show_alert():
    messagebox.showwarning("Warning","This is a warning message.")
def ask_question():
    response=messagebox.askquestion("Question","Do you want to proceed?.")
    if response=="yes":
        print("User wants to proceed.")
    else:
        print("User choose not to proceed")
root=tk.Tk()
info_button=tk.Button(root,text="show Info",command=show_message)
warning_button=tk.Button(root,text="show Warning",command=show_alert)
question_button=tk.Button(root,text="Ask Question",command=ask_question)
info_button.pack()
warning_button.pack()
question_button.pack()
root.mainloop()


