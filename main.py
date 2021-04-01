from helper.serialConnection import SerialConnection

class Application():
     def __init__(self):
         self.connection = SerialConnection()
         
app = Application()