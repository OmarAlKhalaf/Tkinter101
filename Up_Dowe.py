# ========== Start ============ #
from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import CENTER, LEFT, TOP, Button, Label, LabelFrame, ttk


root = tk.Tk()
root.title('Up_down')
root.geometry('400x400')
root.config(bg='grey')
# ======== fonction's ========= #
num = 0


def lab():
    global window, num
    window.config(text=f'{num}')
    if num == 0:
        root.config(bg='grey')
    elif num > 0:
        root.config(bg='green')
    elif num < 0:
        root.config(bg='red')


def plus():
    global num
    print(num)
    num = num + 1
    lab()


def minus():
    global num
    print(num)
    num = num - 1
    lab()
# ======== Code ========= #


# Up Button.
up = Button(root, text="Up", bg='green', fg='white')
up.pack(fill='x', expand=True, ipady=30)
up.config(command=plus)

# Window Label.
window = Label(root, text=f'{num}')
window.pack()

# Down Button.
down = Button(root, text='Down', bg='red', fg='white')
down.pack(fill='x', expand=True, ipady=30)
down.config(command=minus)


# ========== End =========== #
root.mainloop()
