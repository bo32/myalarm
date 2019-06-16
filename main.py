from tkinter import *
from tkinter import ttk

import ui.clock 

root = Tk()
root.attributes("-fullscreen", True) 

def start():
    clock = ui.clock.Clock(root)
    clock.pack()

start()
root.mainloop()
