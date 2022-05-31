import imp
import tkinter as temp
from tkinter import ttk

win=temp.Tk() #

win.title("pyton GUI")
# win.resizable(0, False) #resizable(x-axis,y-axis)
ttk.Label(win, text="라벨").grid(column=0,row=0)
win.mainloop()