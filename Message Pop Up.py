import tkinter as tk
from tkinter import messagebox

class MyClass :
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Message Pop Up")
        
        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Instant Close", command=exit)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Clear textbox", command=self.clear)
        
        self.menubar.add_cascade(menu=self.editmenu, label="Edit")
        
        self.root.config(menu=self.menubar)
        
        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="Show?", font=('Arial', 12), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.Button = tk.Button(self.root, text="Pop my message!", font=('Arial', 12), command=self.show_message)
        self.Button.pack(padx=10, pady=10)
        
        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 16), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else :
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you want to quit the program?"):
            self.root.destroy()
    
    def clear(self):
        self.textbox.delete('1.0', tk.END)
    

MyClass()