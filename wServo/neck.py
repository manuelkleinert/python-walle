from wSerial.write import serialWrite

class Neck:
    def __init__(self, *args):
        self.sw = serialWrite();

    def default(self, speed = 1):
        self.sw.addData({
            'pin': 4,
            'pos': 300,
            'speed': speed
        })

        self.sw.addData({
            'pin': 5,
            'pos': 300,
            'speed': 1
        })

    def up(self, speed = 1):
        self.sw.addData({
            'pin': 4,
            'pos': 500,
            'speed': speed
        })

        self.sw.addData({
            'pin': 5,
            'pos': 500,
            'speed': speed
        })

    def down(self, speed = 1):
        self.sw.addData({
            'pin': 4,
            'pos': 300,
            'speed': speed
        })
    
