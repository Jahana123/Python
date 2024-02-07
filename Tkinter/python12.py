import tkinter as tk
def process_input():
    try:
        user_input=float(entry.get())
        result=user_input*user_input
        output_label.config(text=f"Result: {result}")
    except ValueError:
        output_label.config(text="please enter a valid number")
root=tk.Tk()
root.title("Input Processor")
root.geometry('500x500')
root.configure(bg="lightblue")
label1=tk.Label(root,text="Program to calculate the square of a number",font=('Arial',12),fg='black',bg="lightpink")
label1.grid(row=2,column=4)
label2=tk.Label(root,text="Enter a number")
label2.grid(row=5,column=3)
entry=tk.Entry(root)
entry.grid(row=5,column=4,pady=10)
process_button=tk.Button(root,text="Process",command=process_input)
process_button.grid(row=7,column=4)
output_label=tk.Label(root,text="",bg='lightblue')
output_label.grid(row=9,column=4,pady=10)
root.mainloop()