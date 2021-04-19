from time import sleep
from tkinter import Tk, Frame, Entry, Button, LEFT, BOTTOM
from helper.serialConnection import SerialConnection
from helper.form import Select, TextField

from wSerial.write import SerialWrite

from wServo.neck import Neck
from wServo.head import Head
from wServo.eyes import Eyes
from wServo.arms import Arms
from wMotor.motor import Motor

from wEmotion.happy import Happy


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.wsw = SerialWrite();

        self.eyes = Eyes()
        self.head = Head()
        self.neck = Neck()
        self.arms = Arms()
        self.motor = Motor()

        self.happy = Happy()


        self.servoSelect = Select(self, 'SERVO:', {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', '11':'11', '12':'12', '13':'13', '14':'14'})
        self.servoSelect.setValue('0')

        self.servoInt = TextField(self, 'Go To')
        self.servoInt.setValue(300)
        
        self.servoSpeed = TextField(self, 'Speed')
        self.servoSpeed.setValue(1)

        self.submit = Button(self, text="Submit", command=self.sendForm)
        self.submit.pack()


        frameArmR = Frame(self)
        frameArmR.pack(side = BOTTOM, padx=10, pady=10)

        self.btArUp = Button(frameArmR, text="Arm right UP", command=lambda:self.arms.rightUp())
        self.btArUp.pack(side = LEFT)

        self.btArC = Button(frameArmR, text="Arm right Center", command=lambda:self.arms.rightCenter())
        self.btArC.pack(side = LEFT)

        self.btArDown = Button(frameArmR, text="Arm right Down", command=lambda:self.arms.rightDown())
        self.btArDown.pack(side = LEFT)

        frameArmL = Frame(self)
        frameArmL.pack(side = BOTTOM, padx=10, pady=10)

        self.btAlUp = Button(frameArmL, text="Arm left UP", command=lambda:self.arms.leftUp())
        self.btAlUp.pack(side = LEFT)

        self.btAlC = Button(frameArmL, text="Arm left Center", command=lambda:self.arms.leftCenter())
        self.btAlC.pack(side = LEFT)

        self.btAlDown = Button(frameArmL, text="Arm left Down", command=lambda:self.arms.leftDown())
        self.btAlDown.pack(side = LEFT)


        frameNeck = Frame(self)
        frameNeck.pack(side = BOTTOM, padx=10, pady=10)

        self.btNup = Button(frameNeck, text="Neck UP", command=lambda:self.neck.up(4))
        self.btNup.pack(side = LEFT)

        self.btNd = Button(frameNeck, text="Neck Center", command=lambda:self.neck.center(4))
        self.btNd.pack(side = LEFT)

        self.btNdown = Button(frameNeck, text="Neck Down", command=lambda:self.neck.down(4))
        self.btNdown.pack(side = LEFT)


        frameShow = Frame(self)
        frameShow.pack(side = BOTTOM, padx=10, pady=10)

        self.btNshowUp = Button(frameShow, text="Show Up", command=lambda:self.neck.showUp(3))
        self.btNshowUp.pack(side = LEFT)

        self.btNshowDown = Button(frameShow, text="Show Down", command=lambda:self.neck.showDown(3))
        self.btNshowDown.pack(side = LEFT)

        
        frameHead = Frame(self)
        frameHead.pack(side = BOTTOM, padx=10, pady=10)

        self.btHleft = Button(frameHead, text="Head Left", command=lambda:self.head.left(4))
        self.btHleft.pack(side = LEFT)

        self.btHdefault = Button(frameHead, text="Head Center", command=lambda:self.head.center(4))
        self.btHdefault.pack(side = LEFT)

        self.btHright = Button(frameHead, text="Head Right", command=lambda:self.head.right(4))
        self.btHright.pack(side = LEFT)


        frameEyes = Frame(self)
        frameEyes.pack(side = BOTTOM, padx=10, pady=10)

        self.btEleft = Button(frameEyes, text="Eyes Left", command=lambda:self.eyes.left(4))
        self.btEleft.pack(side = LEFT)

        self.btEdefault = Button(frameEyes, text="Eyes Center", command=lambda:self.eyes.center(4))
        self.btEdefault.pack(side = LEFT)

        self.btEright = Button(frameEyes, text="Eyes Right", command=lambda:self.eyes.right(4))
        self.btEright.pack(side = LEFT)

        self.btEright = Button(frameEyes, text="Eyes Down", command=lambda:self.eyes.down(4))
        self.btEright.pack(side = LEFT)

        self.btEright = Button(frameEyes, text="Eyes Up", command=lambda:self.eyes.up(4))
        self.btEright.pack(side = LEFT)


        frameMotor = Frame(self)
        frameMotor.pack(side = BOTTOM, padx=10, pady=10)

        self.btMleft = Button(frameMotor, text="Motor Left", command=lambda:self.motor.left())
        self.btMleft.pack(side = LEFT)

        self.btMdefault = Button(frameMotor, text="Motor Straight", command=lambda:self.motor.straight())
        self.btMdefault.pack(side = LEFT)
        
        self.btMdefault = Button(frameMotor, text="Motor Back", command=lambda:self.motor.back())
        self.btMdefault.pack(side = LEFT)

        self.btMright = Button(frameMotor, text="Motor Right", command=lambda:self.motor.right())
        self.btMright.pack(side = LEFT)


        frameEmotion = Frame(self)
        frameEmotion.pack(side = BOTTOM, padx=10, pady=10)

        self.btHappyShake = Button(frameEmotion, text="Happy Shake", command=lambda:self.happy.shake())
        self.btHappyShake.pack(side = LEFT)



    def sendForm(self):
        self.wsw.addData({
            'pin': int(self.servoSelect.get()),
            'pos': int(self.servoInt.get()),
            'speed': int(self.servoSpeed.get())
        })

app = Application(Tk())
app.mainloop()