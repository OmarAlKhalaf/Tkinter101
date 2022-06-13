# ===== Start ===== #
from cProfile import label
import tkinter as tk
root = tk.Tk()
root.title('Hello')
root.geometry('200x200')

# Main Code

center_box = tk.Label(
    root,
    text='Hello\nTkinter',
    bg='blue',
    fg='white'
)

center_box.pack(
    ipadx=50,
    ipady=50,
    expand=True
)

# ====== En ===== #
root.mainloop()
