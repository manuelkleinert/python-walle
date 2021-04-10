from wSerial.write import SerialWrite

class Head:
    def __init__(self, *args):
        self.wsw = SerialWrite();

    def center(self, speed = 4):
        self.wsw.addData({
            'pin': 6,
            'pos': 270,
            'speed': speed
        })

    def left(self, speed = 4):
        self.wsw.addData({
            'pin': 6,
            'pos': 380,
            'speed': speed
        })

    def right(self, speed = 4):
        self.wsw.addData({
            'pin': 6,
            'pos': 50,
            'speed': speed
        })
    
