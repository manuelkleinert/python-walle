from time import sleep
from tkinter import Tk, Frame, Entry, Button
from helper.serialConnection import SerialConnection
from helper.form import Select, TextField

from wServo.neck import Neck



class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.neck = Neck()

        self.btNu = Button(master, text="Neck UP", command=self.neck.up)
        self.btNu.pack()

        self.btNd = Button(master, text="Neck Down", command=self.neck.down)
        self.btNd.pack()

        # self.connection = SerialConnection()

        # self.servoSelect = Select(self, 'SERVO:', {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', '11':'11', '12':'12', '13':'13', '14':'14'})
        # self.servoSelect.setValue('0')

        # self.servoInt = TextField(master, 'Go To')
        # self.servoInt.setValue(300)
        # self.servoInt.pack()
        
        # self.servoSpeed = TextField(master, 'Speed')
        # self.servoSpeed.setValue(1)
        # self.servoSpeed.pack()

        # self.serialWriteThread = serialWrite()
        # self.serialWriteThread.start()

        # self.serialReaderThread = serialReader()
        # self.serialReaderThread.start()

        # self.serialWriteThread.setData([
        #     {
        #         'pin': 4,
        #         'pos': 500,
        #         'speed': 1
        #     },{
        #         'pin': 5,
        #         'pos': 500,
        #         'speed': 3
        #     },{
        #         'pin': 6,
        #         'pos': 500,
        #         'speed': 2
        #     }
        # ])


app = Application(Tk())
app.mainloop()