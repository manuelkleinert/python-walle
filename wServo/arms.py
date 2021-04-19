from wSerial.write import SerialWrite

class Arms:
    def __init__(self, *args):
        self.wsw = SerialWrite();


    def rightCenter(self, speed = 8):
            self.wsw.addData({
                'pin': 0,
                'pos': 300,
                'speed': speed
            })

    def rightUp(self, speed = 8):
        self.wsw.addData({
            'pin': 0,
            'pos': 380,
            'speed': speed
        })

    def rightDown(self, speed = 8):
        self.wsw.addData({
            'pin': 0,
            'pos': 200,
            'speed': speed
        })

    def leftCenter(self, speed = 8):
        self.wsw.addData({
            'pin': 1,
            'pos': 300,
            'speed': speed
        })

    def leftUp(self, speed = 8):
        self.wsw.addData({
            'pin': 1,
            'pos': 120,
            'speed': speed
        })

    def leftDown(self, speed = 8):
        self.wsw.addData({
            'pin': 1,
            'pos': 380,
            'speed': speed
        })
    