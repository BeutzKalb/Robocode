import RoboPiLib_pwm as RPL
import time as time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

#pins
ledPin = 1

RPL.pinMode(ledPin,RPL.OUTPUT)



#commands
def blink():
    RPL.digitalWrite(ledPin,1)
    print "The LED is now ON!!"
    time.sleep(0.5)
    RPL.digitalWrite(ledPin,0)
    time.sleep(0.5)
    print "sample text rawr XD"
    RPL.digitalWrite(ledPin,0)
    time.sleep(0.5)
    print "The LED is now OFF"
i = int(raw_input("How many times do u want that light to blink? Type your answer here!>"))
#for n in range(i+1):
    #blink()

def runServo():
    RPL.servoWrite(ledPin,3000)
    print "LED is On!"
    print "Motor is On!"
    time.sleep(3)
    RPL.servoWrite(ledPin,0)
    time.sleep(1)
    print "motor and ledOff"
runServo()
