import sys, glob
from sys import modules
from threading import Thread
from helper.serialConnection import SerialConnection

class serialWrite():
    def __init__(self):
        self.connection = SerialConnection()
        self.running = True

        # Main app
        mainApp = modules['__main__']
        
        # Set serial connection
        if not hasattr(mainApp, 'serialReadThread'):
            mainApp.serialReadThread = Thread(target=self.run)
            mainApp.serialReadThread.start()

        self.serialWrite = mainApp.serialWriteThread

    def run(self):
        while self.running:
            print(self.connection.read())
            sleep(.01)
    
    def stop(self):
        self.running = False

    def start(self):
        self.running = True