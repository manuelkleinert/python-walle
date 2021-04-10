from wSerial.write import SerialWrite

class Neck:
    def __init__(self, *args):
        self.wsw = SerialWrite();

    def center(self, speed = 4):
        self.wsw.addData({
            'pin': 4,
            'pos': 301,
            'speed': speed
        })

        self.wsw.addData({
            'pin': 5,
            'pos': 240,
            'speed': speed
        })

    def up(self, speed = 4):
        self.wsw.addData({
            'pin': 4,
            'pos': 500,
            'speed': speed
        })

        self.wsw.addData({
            'pin': 5,
            'pos': 350,
            'speed': speed
        })

    def down(self, speed = 4):
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
    
    def showUp(self, speed = 3):
        self.wsw.addData({
            'pin': 4,
            'pos': 352,
            'speed': speed
        })

        self.wsw.addData({
            'pin': 5,
            'pos': 160,
            'speed': speed
        })

    def showDown(self, speed = 3):
        self.wsw.addData({
            'pin': 4,
            'pos': 100,
            'speed': speed
        })
        
        self.wsw.addData({
            'pin': 5,
            'pos': 320,
            'speed': speed
        })
