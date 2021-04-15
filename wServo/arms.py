from wSerial.write import SerialWrite

class Arms:
    def __init__(self, *args):
        self.wsw = SerialWrite();


    def rightCenter(self, speed = 5):
            self.wsw.addData({
                'pin': 0,
                'pos': 300,
                'speed': speed
            })

    def rightUp(self, speed = 5):
        self.wsw.addData({
            'pin': 0,
            'pos': 400,
            'speed': speed
        })

    def rightDown(self, speed = 5):
        self.wsw.addData({
            'pin': 0,
            'pos': 200,
            'speed': speed
        })

    def leftCenter(self, speed = 5):
        self.wsw.addData({
            'pin': 1,
            'pos': 300,
            'speed': speed
        })

    def leftUp(self, speed = 5):
        self.wsw.addData({
            'pin': 1,
            'pos': 180,
            'speed': speed
        })

    def leftDown(self, speed = 5):
        self.wsw.addData({
            'pin': 1,
            'pos': 380,
            'speed': speed
        })
    