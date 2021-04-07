import json
from threading import Thread
from time import sleep
from tkinter import Tk, Frame, Entry
from helper.serialConnection import SerialConnection
from helper.form import Select, TextField

class serialReader(Thread):
    def __init__(self, connection, *args):
        Thread.__init__(self)
        self.running = True
        self.connection = connection

    def run(self):
        while self.running:
            print(self.connection.read())
            sleep(.01)
    def stop(self):
        self.running = False

class serialWrite(Thread):
    def __init__(self, connection, *args):
        Thread.__init__(self)
        self.running = True
        self.connection = connection
        self.serialData = []
    def run(self):
        while self.running:
            if not self.serialData:
                continue;
                
            for obj in self.serialData:
                if (not self.connection.write(json.dumps(obj))):
                    print('SEND False')
                    break;
                sleep(0.1)

    def setData(self, serialData = []):
        self.serialData = serialData
    
    def stop(self):
        self.running = False

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.connection = SerialConnection()

        self.servoSelect = Select(self, 'SERVO:', {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', '11':'11', '12':'12', '13':'13', '14':'14'})
        self.servoSelect.setValue('0')

        self.servoInt = TextField(master, 'Go To')
        self.servoInt.setValue(300)
        self.servoInt.pack()
        
        self.servoSpeed = TextField(master, 'Speed')
        self.servoSpeed.setValue(1)
        self.servoSpeed.pack()

        self.serialWriteThread = serialWrite(self.connection)
        self.serialWriteThread.start()

        self.serialReaderThread = serialReader(self.connection)
        self.serialReaderThread.start()

        self.serialWriteThread.setData([
            {
                'pin': 4,
                'pos': 500,
                'speed': 1
            },{
                'pin': 5,
                'pos': 500,
                'speed': 3
            },{
                'pin': 6,
                'pos': 500,
                'speed': 2
            }
        ])


app = Application(Tk())
app.mainloop()