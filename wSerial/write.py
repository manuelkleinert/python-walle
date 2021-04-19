import sys, glob, json
from time import sleep
from sys import modules
from threading import Thread
from helper.serialConnection import SerialConnection
from wSerial.reader import SerialReader

class SerialWrite():
    def __init__(self):
        self.connection = SerialConnection()
        self.wsr = SerialReader()
        self.running = True
        
        # Main app
        self.mainApp = modules['__main__']

        if not hasattr(self.mainApp, 'serialData'):
            self.mainApp.serialData = []
        
        if not hasattr(self.mainApp, 'serialWriteThread'):
            self.mainApp.serialWriteThread = Thread(target=self.run)
            self.mainApp.serialWriteThread.start()

        self.serialWriteThread = self.mainApp.serialWriteThread

    def run(self):
        while self.running:
            if not self.mainApp.serialData:
                continue;
            for i in range(len(self.mainApp.serialData)):

                if(self.mainApp.serialData[i].delay):
                    sleep(self.mainApp.serialData[i].delay)
                    delattr(self.mainApp.serialData[i], 'delay')

                print(self.mainApp.serialData[i])

                if (not self.connection.write(json.dumps(self.mainApp.serialData[i]))):
                    print('SEND False')
                    break;
                    
                sleep(0.2)
                
            self.mainApp.serialData = []

    def addData(self, serialData = []):
        self.mainApp.serialData.append(serialData)
    
    def stop(self):
        self.running = False

    def start(self):
        self.running = True