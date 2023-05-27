from tkinter import *
from tkinter.messagebox import showerror

root = Tk()
root.title("Python Calculator App")
root.geometry('265x500')
root.resizable(0, 0)
root.configure(background='Black')

entry_strvar = StringVar(root)

Label(root, text='Python Calculator App', font=("Helvetica", 15), bg='Black', fg='white').place(x=25, y=0)
Label(root, text='Press \'x\' twice for exponentiation', font=("Georgia", 10), bg='Black',fg='white').place(x=25, y=30)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=22, font=12, state='disabled')
eqn_entry.place(x=10, y=70)

def add_text(text, strvar):
    strvar.set(f'{strvar.get()}{text}')
#Added after repeated NameError
def submit(entry, strvar):
    try:
        result = eval(entry.get())
        strvar.set(result)
    except Exception as e:
        showerror("Error", str(e))

# Number buttons
Button(root, height=2, width=5, text='7', font=9, bg='LightGray', command=lambda: add_text("7", entry_strvar)).place(x=5,
                                                                                                               y=110)

Button(root, height=2, width=5, text='8', font=9, bg='LightGray', command=lambda: add_text("8", entry_strvar)).place(x=65,
                                                                                                               y=110)

Button(root, height=2, width=5, text='9', font=9, bg='LightGray', command=lambda: add_text("9", entry_strvar)).place(x=125,
                                                                                                               y=110)

Button(root, height=2, width=5, text='4', font=9, bg='LightGray', command=lambda: add_text("4", entry_strvar)).place(x=5,
                                                                                                               y=170)

Button(root, height=2, width=5, text='5', font=9, bg='LightGray', command=lambda: add_text("5", entry_strvar)).place(x=65,
                                                                                                               y=170)

Button(root, height=2, width=5, text='6', font=9, bg='LightGray', command=lambda: add_text("6", entry_strvar)).place(x=125,
                                                                                                               y=170)

Button(root, height=2, width=5, text='1', font=9, bg='LightGray', command=lambda: add_text("1", entry_strvar)).place(x=5,
                                                                                                               y=230)

Button(root, height=2, width=5, text='2', font=9, bg='LightGray', command=lambda: add_text("2", entry_strvar)).place(x=65,
                                                                                                               y=230)

Button(root, height=2, width=5, text='3', font=9, bg='LightGray', command=lambda: add_text("3", entry_strvar)).place(x=125,
                                                                                                               y=230)

Button(root, height=2, width=5, text='0', font=9, bg='LightGray', command=lambda: add_text("0", entry_strvar)).place(x=65,
                                                                                                               y=290)

# Operator Buttons
Button(root, height=2, width=5, text='+', font=9, bg='NavyBlue',fg='White', command=lambda: add_text('+', entry_strvar)).place(
    x=195, y=110)

Button(root, height=2, width=5, text='-', font=9, bg='NavyBlue',fg='White', command=lambda: add_text('-', entry_strvar)).place(
    x=195, y=170)

Button(root, height=2, width=5, text='x', font=9, bg='NavyBlue',fg='White', command=lambda: add_text('*', entry_strvar)).place(
    x=195, y=230)

Button(root, height=2, width=5, text='/', font=9, bg='NavyBlue',fg='White', command=lambda: add_text('/', entry_strvar)).place(
    x=195, y=290)

Button(root, height=2, width=5, text='.', font=9, bg='NavyBlue',fg='White', command=lambda: add_text('.', entry_strvar)).place(
    x=5, y=290)

Button(root, height=2, width=5, text='(', font=9, bg='NavyBlue',fg='White', command=lambda: add_text('(', entry_strvar)).place(
    x=125, y=290)

Button(root, height=2, width=5, text=')', font=9, bg='NavyBlue',fg='White', command=lambda: add_text(')', entry_strvar)).place(
    x=125, y=170)

# Equal, C and AC buttons
Button(root, height=2, width=5, text='=', font=9, bg='LightBlue', command=lambda: submit(eqn_entry, entry_strvar)).place(
    x=65, y=350)

Button(root, height=2, width=5, text='C', font=9, bg='DarkRed', command=lambda: entry_strvar.set(entry_strvar.get()[:-1])).place(
    x=125, y=350)

Button(root, height=2, width=5, text='AC', font=9, bg='DarkRed', command=lambda: entry_strvar.set('')).place(x=5, y=350)

Button(root, height=2, width=22, text='Ok', font=9, bg='DarkGrey', fg='Black', command=lambda: root.destroy()).place(x=7, y=425)

root.mainloop()
