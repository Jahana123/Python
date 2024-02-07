import tkinter as tk
def button_click(num):
    global result
    result+=num
    label_result.config(text=result)
def calculate():
      global result
      equation=""
      if result!="":
            try:
                  equation=eval(result)
            except:
                  equation=" Syntax Error!"
                  result=""
      label_result.config(text=equation)
def clear():
       global result
       result=""
       label_result.config(text=result)  
root=tk.Tk()
root.title("Simple calculator program.")
root.geometry('380x430')
root.configure(bg="violet")
result=""
label_result=tk.Label(root,text="",font=("verdana",17,"bold"),bg="white",fg="blue",width=17,height=2,padx=10,pady=10)
label_result.pack()
frame=tk.Frame(root)
frame.pack()
button1=tk.Button(frame,text="7",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("7"))
button1.grid(row=0,column=0)
button2=tk.Button(frame,text="8",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("8"))
button2.grid(row=0,column=1)
button3=tk.Button(frame,text="9",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("9"))
button3.grid(row=0,column=2)
divide=tk.Button(frame,text="/",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("/"))
divide.grid(row=0,column=3)

button4=tk.Button(frame,text="4",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("4"))
button4.grid(row=1,column=0)
button5=tk.Button(frame,text="5",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("5"))
button5.grid(row=1,column=1)
button6=tk.Button(frame,text="6",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("6"))
button6.grid(row=1,column=2)
multiply=tk.Button(frame,text="*",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("*"))
multiply.grid(row=1,column=3)

button7=tk.Button(frame,text="1",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("1"))
button7.grid(row=2,column=0)
button8=tk.Button(frame,text="2",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("2"))
button8.grid(row=2,column=1)
button9=tk.Button(frame,text="3",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("3"))
button9.grid(row=2,column=2)
minus=tk.Button(frame,text="-",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("-"))
minus.grid(row=2,column=3)

button10=tk.Button(frame,text="0",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("0"))
button10.grid(row=3,column=0)
decimal=tk.Button(frame,text=" . ",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("."))
decimal.grid(row=3,column=1)
percntg=tk.Button(frame,text="%",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("%"))
percntg.grid(row=3,column=2)
plus=tk.Button(frame,text="+",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("+"))
plus.grid(row=3,column=3)

button11=tk.Button(frame,text="( ",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click("( "))
button11.grid(row=4,column=0)
button12=tk.Button(frame,text=" )",height=2,width=5,font=("Arail",12,"bold"),bg="black",fg="white",padx=8,pady=8,command=lambda:button_click( ")"))
button12.grid(row=4,column=1)
clear_=tk.Button(frame,text="C",height=2,width=5,bg="#0057D9",fg="white",font=("Arail",12,"bold"),padx=8,pady=8,command=clear)
clear_.grid(row=4,column=2)
equal=tk.Button(frame,text="=",height=2,width=5,bg="#f2450d",fg="white",font=("Arail",12,"bold"),padx=8,pady=8,command=calculate)
equal.grid(row=4,column=3)

root.mainloop()