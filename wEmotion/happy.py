from wSerial.write import SerialWrite

class Happy:
    def __init__(self, *args):
        self.wsw = SerialWrite();

    def shake(self):
        self.wsw.addData({
            'dir': [1,1], # Direction
            'speed': [200, 200],
            'delay': 10
        })

'''     def back(self, speedA = 200, speedB = 200):
        self.wsw.addData({
            'dir': [0,0], # Direction
            'speed': [speedA, speedB]
        })

    def right(self, speed = 200):
        self.wsw.addData({
            'dir': [0,1], # Direction
            'speed': [speed, speed]
        })

    def left(self, speed = 200):
        self.wsw.addData({
            'dir': [1,0], # Direction
            'speed': [speed, speed]
        }) '''