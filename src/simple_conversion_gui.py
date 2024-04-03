import tkinter as tk
import ttkbootstrap as ttk


def main():
    def convert() -> None:
        mile_input = entry_int.get()
        km_output = mile_input * 1.61
        output_string.set(str("{:,.2f}".format(km_output)))

    # creates window
    main_frame = ttk.Window(themename="journal")
    main_frame.title("Demo")
    main_frame.geometry("300x150")

    title_label = ttk.Label(master=main_frame, text="Miles to kilometers", font="Calibre 24 bold")
    # places label in window
    title_label.pack()

    input_frame = ttk.Frame(master=main_frame)
    entry_int = tk.IntVar()
    output_string = tk.StringVar()
    entry_field = ttk.Entry(master=input_frame, textvariable=entry_int)
    button = ttk.Button(master=input_frame, text="Convert", command=convert)
    # pack entry field and button into input frame
    entry_field.pack(side="left", padx=10)
    button.pack(side="left")
    # put input frame into main frame
    input_frame.pack(pady=10)

    output_label = ttk.Label(master=main_frame,
                             text="Output",
                             font="Calibre 24",
                             textvariable=output_string)
    output_label.pack(anchor="s", pady=5)

    # runs the window
    main_frame.mainloop()


if __name__ == "__main__":
    main()
