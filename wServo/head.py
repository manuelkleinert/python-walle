from wSerial.write import SerialWrite

class Head:
    def __init__(self, *args):
        self.wsw = SerialWrite();

    def default(self, speed = 1):
        self.wsw.addData({
            'pin': 6,
            'pos': 300,
            'speed': speed
        })

    def left(self, speed = 1):
        self.wsw.addData({
            'pin': 6,
            'pos': 500,
            'speed': speed
        })

    def right(self, speed = 1):
        self.wsw.addData({
            'pin': 6,
            'pos': 100,
            'speed': speed
        })
    
