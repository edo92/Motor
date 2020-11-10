import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor():
    def __init__(self, Ena, In1, In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(0)

    def moveF(self, speed=50):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)

    def moveB(self, speed=50):
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)


class Action(Motor):
    def __init__(self, direct, row, timeout, speed):
        self.dir = direct
        self.row = row
        self.timeout = int(timeout)
        self.speed = int(speed)

    def row1(self):
        self.motor = Motor(2, 3, 4)

    def row2(self):
        self.motor = Motor(17, 27, 22)

    def run_job(self):
        # Run methods from Motor based on passed argv
        getattr(self.motor, self.dir)(self.speed)

    def run(self):
        # Select motor row from passed argv
        getattr(self, self.row)()
        timeout = time.time() + self.timeout

        while True:
            # Stop on timeout
            if time.time() > timeout:
                self.motor.stop()
                break

            self.run_job()


args = sys.argv[1:]
action = Action(args[0], args[1], args[2], args[3])
action.run()
