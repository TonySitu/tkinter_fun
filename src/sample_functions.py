import tkinter as tk
from tkinter import ttk


def button_func(entry_string):
    print("a button was pressed")
    print(entry_string.get())


def outer_func(param):
    def inner_func():
        print("a button was pressed")
        print(param.get())
    return inner_func


window = tk.Tk()
window.title("buttons, functions and args")

entry_string = tk.StringVar(value='test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text='button', command=outer_func(entry_string))
button.pack()
window.mainloop()
