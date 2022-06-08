# ===== Start ===== #
from cgi import test
from lib2to3.pytree import Leaf
import tkinter as tk
from turtle import left
root = tk.Tk()
root.title('Box demo')
root.geometry('300x200')


# Box 1
box1 = tk.Label(
    root,
    text='Box 1',
    bg='red',
    fg='white'
)

box1.pack(
    ipadx=10,
    ipady=10,
    fill='x'
)

# Box2
box2 = tk.Label(
    root,
    text='Box 2',
    bg='green',
    fg='white'

)

box2.pack(
    ipadx=10,
    ipady=10,
    fill='x',
)

# Box 3
box3 = tk.Label(
    root,
    text='Box 3',
    bg='blue',
    fg='white'
)

box3.pack(
    ipadx=10,
    ipady=10,
    fill='x'
)

# Left Box 4
left_box4 = tk.Label(
    root,
    text='Left',
    bg='cyan',
    fg='black',
)

left_box4.pack(
    ipadx=10,
    ipady=10,
    fill='both',
    expand=True,
    side=tk.LEFT
)
# Center Box 5
center_box5 = tk.Label(
    root,
    text='Center',
    bg='magenta',
    fg='black'
)
center_box5.pack(
    ipadx=10,
    ipady=10,
    fill='both',
    expand=True,
    side=tk.LEFT
)
# Right Box 6
right_box6 = tk.Label(
    root,
    text='Right',
    bg='yellow',
    fg='black'
)
right_box6.pack(
    ipadx=10,
    ipady=10,
    fill='both',
    expand=True,
    side=tk.LEFT
)
# ====== En ===== #
root.mainloop()
