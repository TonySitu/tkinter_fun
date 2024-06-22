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

combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text=f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text='a label', textvariable=food_string)
combo_label.pack()

spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(window,
                   from_=3,
                   to=20,
                   increment=3,
                   command=lambda: print("arrow has been pressed"),
                   textvariable=spin_int)

spin.bind('<<Increment>>', lambda event: print('up"'))
spin.bind('<<Decrement>>', lambda event: print('down"'))
spin.pack()

window.mainloop()
