from wSerial.write import SerialWrite

class Eyes:
    def __init__(self, *args):

        self.wsw = SerialWrite();
        self.pinRight = 8;
        self.pinLeft = 9

    def center(self, speed = 4):
        self.wsw.addData({
            'pin': self.pinRight,
            'pos': 353,
            'speed': speed
        })

        self.wsw.addData({
            'pin': self.pinLeft,
            'pos': 248,
            'speed': speed
        })

    def left(self, speed = 4):
        self.wsw.addData({
            'pin': self.pinRight,
            'pos': 380,
            'speed': speed
        })

        self.wsw.addData({
            'pin': self.pinLeft,
            'pos': 320,
            'speed': speed
        })

    def right(self, speed = 4):
        self.wsw.addData({
            'pin': self.pinRight,
            'pos': 280,
            'speed': speed
        })

        self.wsw.addData({
            'pin': self.pinLeft,
            'pos': 230,
            'speed': speed
        })

    def up(self, speed = 4):
        self.wsw.addData({
            'pin': self.pinRight,
            'pos': 280,
            'speed': speed
        })

        self.wsw.addData({
            'pin': self.pinLeft,
            'pos': 320,
            'speed': speed
        })

    def down(self, speed = 4):
        self.wsw.addData({
            'pin': self.pinRight,
            'pos': 380,
            'speed': speed
        })

        self.wsw.addData({
            'pin': self.pinLeft,
            'pos': 230,
            'speed': speed
        })