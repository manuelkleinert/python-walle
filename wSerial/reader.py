import sys, glob
from sys import modules
from time import sleep
from threading import Thread
from helper.serialConnection import SerialConnection

class SerialReader():
    def __init__(self):
        self.connection = SerialConnection()
        self.running = True

        # Main app
        mainApp = modules['__main__']
        
        if not hasattr(mainApp, 'serialReadThread'):
            mainApp.serialReadThread = Thread(target=self.run)
            mainApp.serialReadThread.start()

        self.serialReadThread = mainApp.serialReadThread

    def run(self):
        while self.running:
            print(self.connection.read())
            sleep(.01)
    
    def stop(self):
        self.running = False

    def start(self):
        self.running = True