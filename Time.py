# ========= Start ======== #
from cProfile import label
import tkinter as tk
from time import strftime
root = tk.Tk()
root.title('Clock')

# ========= Def ========== #


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# ========= Code ========= #
lbl = tk.Label(root, font=('caliberi', 40, 'bold'), bg='black', fg='white')

lbl.pack(anchor='center')
time()
# ======== End =========== #
root.mainloop()
