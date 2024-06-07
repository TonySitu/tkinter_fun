import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")


def button_func():
    print(radio_var.get())


button_string = tk.StringVar(value="A button with string var")
button = ttk.Button(window, text="A button", command=button_func, textvariable=button_string)
button.pack()

check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(window, text="checkbox1", command=lambda: print(check_var.get()), variable=check_var, onvalue=5,
                        offvalue=10)
check.pack()

radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text="radio1", value="radio1", variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text="radio2", value="2", variable=radio_var)
radio2.pack()

window.mainloop()
