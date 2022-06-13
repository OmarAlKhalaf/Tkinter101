from cgitb import text
from logging import root
import tkinter as tk
from tkinter import LEFT, TOP, Button, Label, ttk
from tkinter import messagebox
root = tk.Tk()


# ==============Start=============== #
root.title('Test wendow')
root.geometry('300x400')
# ========= Fonction here ========== #


def clicker(event1):
    mylabel = Label(root, text='You cklicked a button')
    mylabel.pack()


# ========= Action ================= #
box = Button(root, text='Click me')
box.bind('<Button-3>', clicker)
box.pack(ipady=20)


# =============End=============== #

root.mainloop()
num = 0
