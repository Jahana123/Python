import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

connection=sql.connect('todo_list.db')
cursor=connection.cursor()
cursor.execute("create table if not exists tasks(task_id int primary key autoincrement,task_description text not null)")
connection.commit()

def add_task():
    task=entry.get()
    if task:
        cursor.execute("insert into tasks (task_description) values (?)",(task,))
        connection.commit()
        update_task_list()
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","Please enter a task!")


def delete_task():
    try:
       selected_task=listbox.curselection()[0]
       task_id=task_ids[selected_task]
       cursor.execute("delete from tasks where task_id=?",(task_id,))
       connection.commit()
       update_task_list()
    except IndexError:
        messagebox.showwarning("warning","please select a task to delete!")
 
def delete_all_tasks():
            cursor.execute("delete from tasks")
            connection.commit()
            update_task_list()

def exit():
     root.destroy()
    
def update_task_list():
     listbox.delete(0,tk.END)
     global task_ids
     task_ids=[]
     cursor.execute("select * from tasks")
     for row in cursor.fetchall():
          task_ids.append(row[0])
          listbox.insert(tk.END,row[1])

root=tk.Tk()
root.title("To-Do List")
root.geometry("900x470")
root.resizable(0,0)
root.configure(bg="white")

frame=tk.Frame(root,bg="black")
frame.pack(side="top",expand=True,fill="both")

l1=tk.Label(frame,text="Enter the Task : ",font=("arial",14,"bold"),bg="black",fg="white")
l1.place(x=19,y=25)

entry=tk.Entry(frame,font=("arial",14,"bold"),width=61,fg="black",bg="white")
entry.place(x=195,y=27)

add_button=tk.Button(frame,text="Add Task",width=20,bg="#D4AC0D",font=("arial",14,"bold"),command=add_task)
add_button.place(x=18,y=80)

delete_button=tk.Button(frame,text="Delete Task",width=20,bg="#D4AC0D",font=("arial",14,"bold"),command=delete_task)
delete_button.place(x=310,y=80)

delete_all_button=tk.Button(frame,text="Delete All Tasks",width=22,font=("arial",14,"bold"),bg="#D4AC0D",command=delete_all_tasks)
delete_all_button.place(x=600,y=80)

listbox=tk.Listbox(frame,width=95,height=11,font=("arial",12,"bold"),selectmode="SINGLE",bg="white",fg="black")
listbox.place(x=17,y=140)

exit_button=tk.Button(frame,text="Exit",width=71,bg="#D4AC0D",font=("arial",14,"bold"),command=exit)
exit_button.place(x=16,y=390)

update_task_list()

root.mainloop()

connection.close()