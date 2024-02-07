import tkinter as tk
root=tk.Tk()
root.geometry('1800x1200')
def button_click():
    print('button clicked')
label=tk.Label(root,text="Welcome to tkinter")
button=tk.Button(root,text="click me",command=button_click)
entry=tk.Entry(root)
label.pack()
button.pack()
entry.pack()
root.mainloop()

