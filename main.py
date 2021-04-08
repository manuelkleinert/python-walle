from time import sleep
from tkinter import Tk, Frame, Entry, Button
from helper.serialConnection import SerialConnection
from helper.form import Select, TextField

from wServo.neck import Neck
from wServo.head import Head

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.head = Head()
        self.neck = Neck()

        self.head.center()
        self.neck.down()

        self.btNup = Button(master, text="Neck UP", command=lambda:self.neck.up(3))
        self.btNup.pack()

        self.btNd = Button(master, text="Neck Center", command=lambda:self.neck.center(3))
        self.btNd.pack()

        self.btNdown = Button(master, text="Neck Down", command=lambda:self.neck.down(3))
        self.btNdown.pack()

        self.btNshowUp = Button(master, text="Show Up", command=lambda:self.neck.showUp(3))
        self.btNshowUp.pack()

        self.btNshowDown = Button(master, text="Show Down", command=lambda:self.neck.showDown(3))
        self.btNshowDown.pack()

        self.btHleft = Button(master, text="Head Left", command=lambda:self.head.left(3))
        self.btHleft.pack()

        self.btHdefault = Button(master, text="Head Center", command=lambda:self.head.center(3))
        self.btHdefault.pack()

        self.btHright = Button(master, text="Head Right", command=lambda:self.head.right(3))
        self.btHright.pack()


app = Application(Tk())
app.mainloop()