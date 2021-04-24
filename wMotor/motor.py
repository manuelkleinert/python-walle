from wSerial.write import SerialWrite

class Motor:
    def __init__(self, *args):

        self.wsw = SerialWrite();

    def straight(self, speedA = 150, speedB = 150, loopCount = 2):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [1,1], # Direction
                'speed': [speedA, speedB]
            })

    def back(self, speedA = 150, speedB = 150, loopCount = 2):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [0,0], # Direction
                'speed': [speedA, speedB]
            })

    def right(self, speed = 150, loopCount = 1):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [0,1], # Direction
                'speed': [speed, speed]
            })

    def left(self, speed = 150, loopCount = 1):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [1,0], # Direction
                'speed': [speed, speed]
            })