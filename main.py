from time import sleep
from tkinter import Tk, Frame, Entry, Button, LEFT, BOTTOM
from helper.serialConnection import SerialConnection
from helper.form import Select, TextField
from wSerial.write import SerialWrite

from wServo.neck import Neck
from wServo.head import Head

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.wsw = SerialWrite();

        self.head = Head()
        self.neck = Neck()


        self.servoSelect = Select(self, 'SERVO:', {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', '11':'11', '12':'12', '13':'13', '14':'14'})
        self.servoSelect.setValue('0')

        self.servoInt = TextField(self, 'Go To')
        self.servoInt.setValue(300)
        
        self.servoSpeed = TextField(self, 'Speed')
        self.servoSpeed.setValue(1)

        self.submit = Button(self, text="Submit", command=lambda:self.wsw.addData({
            'pin': self.servoSelect.get(),
            'pos': self.servoInt.get(),
            'speed': self.servoSpeed.get()
        }))
        self.submit.pack()

        frameNeck = Frame(self)
        frameNeck.pack(side = BOTTOM, padx=10, pady=10)

        self.btNup = Button(frameNeck, text="Neck UP", command=lambda:self.neck.up(3))
        self.btNup.pack(side = LEFT)

        self.btNd = Button(frameNeck, text="Neck Center", command=lambda:self.neck.center(3))
        self.btNd.pack(side = LEFT)

        self.btNdown = Button(frameNeck, text="Neck Down", command=lambda:self.neck.down(3))
        self.btNdown.pack(side = LEFT)


        frameShow = Frame(self)
        frameShow.pack(side = BOTTOM, padx=10, pady=10)

        self.btNshowUp = Button(frameShow, text="Show Up", command=lambda:self.neck.showUp(3))
        self.btNshowUp.pack(side = LEFT)

        self.btNshowDown = Button(frameShow, text="Show Down", command=lambda:self.neck.showDown(3))
        self.btNshowDown.pack(side = LEFT)

        
        frameHead = Frame(self)
        frameHead.pack(side = BOTTOM, padx=10, pady=10)

        self.btHleft = Button(frameHead, text="Head Left", command=lambda:self.head.left(3))
        self.btHleft.pack(side = LEFT)

        self.btHdefault = Button(frameHead, text="Head Center", command=lambda:self.head.center(3))
        self.btHdefault.pack(side = LEFT)

        self.btHright = Button(frameHead, text="Head Right", command=lambda:self.head.right(3))
        self.btHright.pack(side = LEFT)


app = Application(Tk())
app.mainloop()