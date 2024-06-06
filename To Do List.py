import tkinter as tk
from tkinter import messagebox

class MyClass():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("700x800")
        self.root.title("To Do List")
        
        # Header
        
        self.label = tk.Label(self.root, text="To Do List", font=('Arial', 24))
        self.label.pack(padx=10, pady=10)
        
        # Menu
        
        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Save")
        
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Enter", command=self.enter)
        self.editmenu.add_command(label="Delete", command=self.delete)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.editmenu, label="Edit")
        
        self.root.config(menu=self.menubar)
        
        # Textbox widget for user input
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.frame, height=1, font=('Arial', 20))
        self.textbox.grid(row=0, column=0, padx=5)
        
        # Add button
        
        self.add = tk.Button(self.frame, text="Add", font=('Arial', 16), command=self.enter)
        self.add.grid(row=0, column=1, sticky="ew")
        
        self.frame.columnconfigure(0, weight=1)
        
        # Box for list of tasks
        
        self.task_list = tk.Listbox(self.root, font=('Arial', 16), selectmode=tk.SINGLE)
        self.task_list.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Delete button
        
        self.deletebutton = tk.Button(self.frame, text="Delete", font=('Arial', 16), command=self.delete)
        self.deletebutton.grid(row=0, column=2, sticky="ew")
        
        # Keybinds for enter and delete
        
        self.root.bind('<Return>', self.enter_key_pressed)
        
        self.root.bind('<BackSpace>', self.del_key_pressed)
        
        # Calling main()
        
        self.root.mainloop()
        
    def enter(self):
        task = self.textbox.get('1.0', tk.END).strip()
        
        if task:
            self.task_list.insert(tk.END, task)
            self.textbox.delete('1.0', tk.END)
        
        else :
            messagebox.showinfo(title="Message", message="Please enter a non-empty task.")
            
    def delete(self):
        select = self.task_list.curselection()
        
        if select:
            self.task_list.delete(select)

    def enter_key_pressed(self, event):
        
        self.enter()
        return "break"
    
    def del_key_pressed(self, event):
        
        self.delete()
        return "break"
        
MyClass()