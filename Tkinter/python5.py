import tkinter as tk
def get_selected_item():
    selected_item=listbox.get(tk.ACTIVE)
    print("selected item: ",selected_item)
root=tk.Tk()
root.geometry('500x500')
listbox=tk.Listbox(root)
listbox.pack()
for item in ['option 1','option 2','option 3']:
    listbox.insert(tk.END,item)
button=tk.Button(root,text='get selected item', command=get_selected_item)
button.pack()
root.mainloop()