import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("600x400")
window.title("Combo and Spin")

items = ("Ice cream", "Pizza", "Brocoli")
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items

combo.pack()

combo.bind("<<ComboboxSelected>>", lambda event: print("test"))

window.mainloop()
