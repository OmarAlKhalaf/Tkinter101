from cgitb import text
from logging import root
import tkinter as tk
from tkinter import LEFT, TOP, Button, Label, ttk
from tkinter import messagebox

root = tk.Tk()

# ==============Start=============== #
root.title('Test wendow')
root.geometry('300x400')
root.resizable(False, False)

# ========= Fonction here ========== #


def Info():
    respon = messagebox.showinfo('Info', ' Boo!')
    if respon == 'Ok' or respon == 'ok':
        Label(root, text='Fine...').pack(10)


def error():
    respon = messagebox.showerror('Error', 'Hehe')
    Label(root, text=respon).pack()


def warning():
    respon = messagebox.showwarning('Warning', 'Owf owf ')
    Label(root, text=respon).pack()


def question():
    respon = messagebox.askquestion('Question', 'Hmmm')
    Label(root, text=respon).pack()


def yes_no():
    respon = messagebox.askyesno('Yes_No', 'OK')
    Label(root, text=respon).pack()


def cancel():
    respon = messagebox.askokcancel('Cancel', 'Daaa')
    Label(root, text=respon).pack()


# Button 1 #
Button(
    root,
    text='This is a info message',
    command=Info).pack(ipady=10)

# Button 2 #
Button(
    root,
    text='This is a error message',
    command=error).pack(ipady=10)

# Button 3 #
Button(
    root,
    text='This is a Warning message',
    command=warning).pack(ipady=10)

# Button 4 #
Button(
    root,
    text='This is a question message',
    command=question).pack(ipady=10)

# Button 5 #
Button(
    root,
    text='This is a Yes_No message',
    command=yes_no).pack(ipady=10)

# Button 6 #
Button(
    root,
    text='This is a cancel message',
    command=cancel).pack(ipady=10)

# =============End=============== #

root.mainloop()
