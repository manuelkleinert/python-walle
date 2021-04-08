import sys, glob, json
from time import sleep
from sys import modules
from threading import Thread
from helper.serialConnection import SerialConnection

class serialWrite():
    def __init__(self):
        self.connection = SerialConnection()
        self.running = True
        self.serialData = []
        
        # Main app
        mainApp = modules['__main__']
        
        # Set serial connection
        if not hasattr(mainApp, 'serialWriteThread'):
            mainApp.serialWriteThread = Thread(target=self.run)
            mainApp.serialWriteThread.start()

        self.serialWrite = mainApp.serialWriteThread

    def run(self):
        while self.running:
            if not self.serialData:
                continue;
                
            for i in range(len(self.serialData)):
                print('SEND :::::')
                print(self.serialData[i])
                if (not self.connection.write(json.dumps(self.serialData[i]))):
                    print('SEND False')
                    break;
                # self.serialData.pop(i)
                sleep(0.1)

    def addData(self, serialData = []):
        self.serialData.append(serialData)
    
    def stop(self):
        self.running = False

    def start(self):
        self.running = True