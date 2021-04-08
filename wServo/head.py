from wSerial.write import SerialWrite

class Head:
    def __init__(self, *args):
        self.wsw = SerialWrite();
        print("Head init");

    def center(self, speed = 1):
        print("Head D")
        self.wsw.addData({
            'pin': 6,
            'pos': 310,
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
    
