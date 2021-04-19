from time import sleep
from wSerial.write import SerialWrite

from wServo.neck import Neck
from wServo.head import Head
from wServo.eyes import Eyes
from wServo.arms import Arms
from wMotor.motor import Motor

class Happy:
    def __init__(self, *args):
        self.wsw = SerialWrite();

        self.eyes = Eyes()
        self.head = Head()
        self.neck = Neck()
        self.arms = Arms()
        self.motor = Motor()

    def shake(self):
        self.eyes.down()
        sleep(.5)

        self.arms.leftUp()
        sleep(.5)
        self.arms.rightUp()

        sleep(.5)
        self.eyes.up()

        sleep(.5)
        self.motor.right(200)
        sleep(.2)
        self.motor.left(200)
        sleep(.2)
        self.motor.right(200)
        sleep(.2)
        self.motor.left(200)
        sleep(.2)
        self.motor.right(200)

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