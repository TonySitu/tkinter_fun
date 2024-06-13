import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f"x: {event.x} y: {event.y}")


window = tk.Tk()
window.geometry("600x500")
window.title("event binding")

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="A Button")
button.pack()

button.bind("<Alt-KeyPress-a>", lambda event: print(event))
text.bind("<Motion>", get_pos)
window.bind("<KeyPress>", lambda event: print(event.char + " was pressed"))
entry.bind("<FocusIn>", lambda event: print("entry field was selected"))


window.mainloop()
