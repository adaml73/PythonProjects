#tkinter experiment for sine wave solver
#eventually to be used in conjnction w/ sineW.py for complete app

#!/usr/bin/python/
#from Tkinter import *
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
#IntVar = 2
#var = IntVar()
v = stringVar()

e = Entry(master, textvariable = v)
e.pack()

v.set("a default value")
s = v.get
def helloCallBack():
    tkMessageBox.showinfo("Hello python", "hello World")

def alsoCallBack():
    tkMessageBox.showinfo("also Hello", "this is a message box")


#def quitCallBack():
C1 = Checkbutton(top, text = "Music", variable = var, onValue = 1, \
offValue = 0, height = 5, width = 20)

#e = Entry(master)

w = Tkinter.Button(top, text = "hello", fg = "red", command = helloCallBack)
m = Tkinter.Button(top, text = "also hello", command = alsoCallBack)

w.pack()
m.pack()
C1.pack()
top.mainloop()
