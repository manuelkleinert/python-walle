from wSerial.write import SerialWrite

class Motor:
    def __init__(self, *args):

        self.wsw = SerialWrite();

    def straight(self, speedA = 200, speedB = 200, loopCount = 1):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [1,1], # Direction
                'speed': [speedA, speedB]
            })
            sleep(0.2)

    def back(self, speedA = 200, speedB = 200, loopCount = 1):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [0,0], # Direction
                'speed': [speedA, speedB]
            })
            sleep(0.2)

    def right(self, speed = 200, loopCount = 1):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [0,1], # Direction
                'speed': [speed, speed]
            })
            sleep(0.2)

    def left(self, speed = 200, loopCount = 1):
        for x in range(loopCount):
            self.wsw.addData({
                'dir': [1,0], # Direction
                'speed': [speed, speed]
            })
            sleep(0.2)