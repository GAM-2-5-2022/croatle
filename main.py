from tkinter import *
from tkinter import ttk

gui = Tk(className='Python Examples - Window Size')
gui.geometry("720x480")
frm = ttk.Frame(gui, padding=10)
frm.grid()
ttk.Label(frm, text="Croatle").grid(column=0, row=0)

gui.mainloop() 
