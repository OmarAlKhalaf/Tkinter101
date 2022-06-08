from time import sleep
import tkinter as tk
from threading import Timer

# ======================= main setup ==========
main = tk.Tk()
main.title('First window')
counter = 6
coler = {
    '50x50': 'purple',
    '100x100': 'red',
    '150x150': 'blue',
    '200x200': 'green',
    '250x250': 'yellow',
    '300x300': 'black',
}
# ======== functions hieronder ========#


def update():
    global counter
    for s in coler:
        main.geometry(s)
        main.config(bg=coler[s])
        print(f'update {counter}')
        counter -= 1
        sleep(2)
        if coler[s] == 'black':
            print('Boom!')
            main.destroy()


Timer(0, update).start()

#============== End ===============#
main.mainloop()
