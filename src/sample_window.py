import tkinter as tk
import ttkbootstrap as ttk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ttk_entry_string = ttk.StringVar()
        self.ttk_label = None
        self.ttk_text = None
        self.ttk_entry = None
        self.ttk_button = None
        self.__create_window()

    def __create_window(self):
        self.title("Window and widgets experimentation")
        self.geometry('800x500')

        self.ttk_label = ttk.Label(master=self, text="Test label")
        self.ttk_label.pack()

        self.ttk_entry = ttk.Entry(master=self)
        self.ttk_entry.pack()

        tk.Label(master=self, text="my label").pack()

        self.ttk_button = ttk.Button(master=self, textvariable=self.ttk_entry_string,
                                     command=lambda: self.ttk_entry_string.set(self.ttk_entry.get()))
        self.ttk_button.pack()


def main():
    window = View()
    window.mainloop()


if __name__ == "__main__":
    main()
