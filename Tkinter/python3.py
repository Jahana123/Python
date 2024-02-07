import tkinter as tk
root=tk.Tk()
root.geometry('1800x1200')
checkbox=tk.Checkbutton(root,text='Option 1')
radio_button1=tk.Radiobutton(root,text='Option 2')
radio_button2=tk.Radiobutton(root,text='Option 3')
checkbox.pack()
radio_button1.pack()
radio_button2.pack()
root.mainloop()

