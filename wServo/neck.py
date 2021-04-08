from wSerial.write import SerialWrite

class Neck:
    def __init__(self, *args):
        self.wsw = SerialWrite();

    def default(self, speed = 1):
        self.wsw.addData({
            'pin': 4,
            'pos': 300,
            'speed': speed
        })

        self.wsw.addData({
            'pin': 5,
            'pos': 300,
            'speed': 1
        })

    def up(self, speed = 1):
        self.wsw.addData({
            'pin': 4,
            'pos': 500,
            'speed': speed
        })

        self.wsw.addData({
            'pin': 5,
            'pos': 500,
            'speed': speed
        })

    def down(self, speed = 1):
        self.wsw.addData({
            'pin': 4,
            'pos': 100,
            'speed': speed
        })

        self.wsw.addData({
            'pin': 5,
            'pos': 100,
            'speed': speed
        })
    
