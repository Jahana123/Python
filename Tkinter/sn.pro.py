import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
class TextEditor:
    def __init__(self, root):
        self.root = root
        root.title("PROJECT")
        root.geometry('1000x600')
        
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        self.text_widget = tk.Text(root,height=1000,width=600)
        self.text_widget.pack()
        self.text_widget.insert(tk.END," ")

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Close", command=self.close_file)
        self.file_menu.add_command(label="Exit", command=root.destroy)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)
        self.root.title(" ")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)
        

    def save_as_file(self):
        self.save_file()

    def close_file(self):
        self.text_widget.delete(1.0, tk.END)
        self.root.title("PROJECT")
    
    def exit_app(self):
        self.root.destroy()
    

if __name__=="__main__":
    editor = TextEditor(root)
    root.mainloop()