import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    km_output = float("{:.2f}".format(km_output))  # precision set to 2
    string = f"{mile_input} miles = {km_output} kilometers."
    output_string.set(string)


# window
window = ttk.Window(themename='journal')
window.title('Converter')
window.geometry('300x150')

# title
title_label = ttk.Label(master=window, text='Enter Miles:', font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Output',
                         font='Calibri 14',
                         textvariable=output_string)
output_label.pack(pady=10)

# run
window.mainloop()
