import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry("300x150")

def convert():
    # output_string = entry_int.get()*1,609344
    result = entry_int.get()*1.609344
    output_string.set(value=result)

# title
title_label = ttk.Label(master=window, text="Miles to kilometers", font='Calibri 12 bold')
title_label.pack(pady=5)

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert',command=convert)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font='Calibri 12', textvariable=output_string)
output_label.pack(pady=5)

# run
window.mainloop()