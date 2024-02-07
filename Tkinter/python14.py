import tkinter as tk
def button_click(button_value):
            current=str(entry.get())
            entry.delete(0,tk.END)
            entry.insert(0,current + button_value)
def clear():
            entry.delete(0,tk.END)
def calculate():
        try:
                result=eval(entry.get())
                entry.delete(0,tk.END)
                entry.insert(0,str(result))
        except:
                entry.delete(0,tk.END)
                entry.insert(0,"Error")
root=tk.Tk()
root.title("Simple calculator")
root.geometry("300x300")
root.configure(bg='lightpink')
entry=tk.Entry(root,width=28)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','%','+'
]
row,col=1,0
for button in buttons:
    tk.Button(root,text=button,width=5,height=2,font=("Arial",10),bg="grey",fg="white", command=lambda b=button:button_click(b)).grid(row=row,column=col)
    col+=1
    if col>3:
        col=0
        row+=1
tk.Button(root,text="C", width=5,height=2,font=("Arial",10),bg="red",fg="white",command=clear).grid(row=row,column=col)
col+=1
tk.Button(root,text="=", width=5,height=2,font=("Arial",10),bg="green", fg="white",command=calculate).grid(row=row,column=col)
root.mainloop()

