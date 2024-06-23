import tkinter as tk
from tkinter import ttk


def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-brush_size/2, y-brush_size/2, x+brush_size/2, y+brush_size/2, fill='black')


def adjust_brush_size(event):
    global brush_size
    if event.delta > 0:
        brush_size = min(brush_size + 4, 12)
        print(brush_size)
    else:
        brush_size = max(0, brush_size - 4)


window = tk.Tk()
window.geometry('600x400')
window.title("Canvas")

canvas = tk.Canvas(window, bg='white')
canvas.pack()

brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', adjust_brush_size)

window.mainloop()
