from wSerial.write import SerialWrite

class Arms:
    def __init__(self, *args):
        self.wsw = SerialWrite();


    def rightCenter(self, speed = 4):
            self.wsw.addData({
                'pin': 0,
                'pos': 290,
                'speed': speed
            })
        
    def leftCenter(self, speed = 4):
            self.wsw.addData({
                'pin': 1,
                'pos': 290,
                'speed': speed
            })

    def rightUp(self, speed = 4):
        self.wsw.addData({
            'pin': 0,
            'pos': 380,
            'speed': speed
        })

    def rightDown(self, speed = 4):
        self.wsw.addData({
            'pin': 0,
            'pos': 200,
            'speed': speed
        })
    