from threading import Thread
from time import sleep
from tkinter import Tk, Frame, Entry
from helper.serialConnection import SerialConnection
from helper.form import Select

class serialReader(Thread):
    def __init__(self, connection, *args):
        Thread.__init__(self)
        self.running = True
        self.connection = connection

    def run(self):
        while self.running:
            print(self.connection.read())
            sleep(.1)
    def stop(self):
        self.running = False

class serialWrite(Thread):
    def __init__(self, connection, servoSelect, servoInt, *args):
        Thread.__init__(self)
        self.running = True
        self.connection = connection
        self.servoSelect = servoSelect
        self.servoInt = servoInt
        self.servoPos = "300"

        print("POS:::")
        print(self.servoPos)

    def run(self):
        while self.running:
            self.servoPos = self.servoInt.get()

            if self.servoPos == "":
                print('reset')
                self.servoPos = "300"

            if (not self.connection.write("{\"Servo\":" + self.servoSelect.get() + ",\"Pos\":" + self.servoPos +"}")):
                print('SEND False')
            sleep(1)
    def stop(self):
        self.running = False

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.connection = SerialConnection()

        self.servoSelect = Select(self, 'SERVO:', {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', '11':'11', '12':'12', '13':'13', '14':'14'})
        self.servoSelect.setValue('0')

        self.servoInt = Entry(master)
        self.servoInt.pack()

        self.serialWriteThread = serialWrite(self.connection, self.servoSelect, self.servoInt)
        self.serialWriteThread.start()

        self.serialReaderThread = serialReader(self.connection)
        self.serialReaderThread.start()

        


app = Application(Tk())
app.mainloop()