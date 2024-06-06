import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Exploring GUI")

label = tk.Label(root, text="Python Programming", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10)

buttonframe = tk.Frame(root) #frame inside root
buttonframe.columnconfigure(0, weight=1) #Establishing 3 columns
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="7", font=("Arial", 18))
btn7.grid(row=3, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text="8", font=("Arial", 18))
btn8.grid(row=3, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text="9", font=("Arial", 18))
btn9.grid(row=3, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()