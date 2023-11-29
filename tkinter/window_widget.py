import tkinter as tk
from tkinter import ttk

def press_button():
    print("A button was pressed")
    
# create a window
window = tk.Tk()
window.title("Window and Widgets")

# widthxheight
window.geometry("800x500")

# create widgets

## ttk label
label = ttk.Label(master=window,text="This is a label")
label.pack()

## tk.text (text box / text area)
text = tk.Text(master=window)
text.pack()

## ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# exercise label
exercise_label = ttk.Label(master=window,text="My button")
exercise_label.pack()

## ttk button
button = ttk.Button(master=window,text="This is a button",command=press_button)
button.pack()

# exercise
# add one more text label and a button with a function that prints 'hello'
# the label should say 'my label' and be between the entry widget and button

# exercise button
exercise_button = ttk.Button(master=window,text="Say hello!",command=lambda: print("hello"))
exercise_button.pack()

# run
window.mainloop()