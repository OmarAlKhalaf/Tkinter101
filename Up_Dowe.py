# ========== Start ============ #
from cProfile import label
import tkinter as tk
from tkinter import CENTER, LEFT, TOP, Button, Label, LabelFrame, ttk
root = tk.Tk()
root.title('Up_down')
root.geometry('400x400')
# ======== fonction's ========= #


# def num():
#     pass

# ======== Code ========= #


# Up Button.
up = Button(
    root,
    text="Up",
    bg='green',
    fg='white'
).pack(fill='x', expand=True, ipady=30)


# Down Button.
down = Button(
    root,
    text='Down',
    bg='red',
    fg='white'
).pack(fill='x', expand=True, ipady=30)


# ========== End =========== #
root.mainloop()
