from wSerial.write import SerialWrite

class Arms:
    def __init__(self, *args):
        self.wsw = SerialWrite();


    def rightCenter(self, speed = 1):
            self.wsw.addData({
                'pin': 0,
                'pos': 300,
                'speed': speed
            })

    def rightUp(self, speed = 1):
        self.wsw.addData({
            'pin': 0,
            'pos': 380,
            'speed': speed
        })

    def rightDown(self, speed = 1):
        self.wsw.addData({
            'pin': 0,
            'pos': 220,
            'speed': speed
        })

    def leftCenter(self, speed = 1):
        self.wsw.addData({
            'pin': 1,
            'pos': 300,
            'speed': speed
        })

    def leftUp(self, speed = 1):
        self.wsw.addData({
            'pin': 1,
            'pos': 120,
            'speed': speed
        })

    def leftDown(self, speed = 1):
        self.wsw.addData({
            'pin': 1,
            'pos': 360,
            'speed': speed
        })
    