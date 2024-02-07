import tkinter as tk
root=tk.Tk()
root.geometry('300x300')
text_widget=tk.Text(root,height=5,width=30)
text_widget.pack()
text_widget.insert(tk.END,'Type your message here...')
message_widget=tk.Message(root,text='This is a message widget.',width=150)
message_widget.pack()
root.mainloop()