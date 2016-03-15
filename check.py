

from Tkinter import *
master = Tk()
v = IntVar()

c = Checkbutton(master, text = "Expand", variable = v)
c.var = v
#c.pack()

#def __init__(self, master):
    #self.var = IntVar()
    #m = Checkbutton(
        #master, text = "Enable Tab", variable = self.var,
        #command = self.cb)
    #m.pack()

#def cb(self, event):
    #print "variable is", self.var.get()




mainloop()
