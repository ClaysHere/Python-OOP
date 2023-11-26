from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

app = Tk()
app.configure(bg="white")
app.resizable(False,False)
app.geometry("400x400")
app.title("Toko Buku")
FIRST_NAME = StringVar()
LAST_NAME = StringVar()

# input frmae
frm = ttk.Frame(app,padding=12)

# penempatan Grid, Pack, Place
frm.pack(padx=10,pady=10, fill="x", expand=True)

# komponen - komponen
# 1. Label
first_name_label = ttk.Label(frm,text="First Name :")
first_name_label.pack(padx=10, fill="x", expand=True)
# 2. Entry
first_name_entry = ttk.Entry(frm,textvariable=FIRST_NAME)
first_name_entry.pack(padx=10, fill="x", expand=True)

# 1. Label
last_name_label = ttk.Label(frm,text="Last Name :")
last_name_label.pack(padx=10, fill="x", expand=True)
# 2. Entry
last_name_entry = ttk.Entry(frm,textvariable=LAST_NAME)
last_name_entry.pack(padx=10, fill="x", expand=True)

def helo():
    print(f"Hi {FIRST_NAME.get()} {LAST_NAME.get()}!")
    showinfo(title='Message', message=f"Hi {FIRST_NAME.get()} {LAST_NAME.get()}!")
    

greetings = ttk.Button(frm,text='Greetings',command=helo)
greetings.pack(fill='x',expand=True,pady=10,padx=10)

app.mainloop()