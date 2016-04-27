#! /usr/bin/python3

import os,sys
from tkinter import *
#from tkinter.ttk import *

root = Tk()
root.title("My Application")
program_directory=sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "myicon.png")))
root.mainloop()
