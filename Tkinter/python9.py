import tkinter as tk
root=tk.Tk()
root.geometry('200x200')
label1=tk.Label(root,text='Label1')
label2=tk.Label(root,text='Label2')
label3=tk.Label(root,text='Label3')
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0,columnspan=2)
root.mainloop()

