import pcf8574_io
import RPi.GPIO as GPIO
import configparser
import os
from time import sleep
import sys


class Buttons:
    def __init__(self, vm):
        self.parent = vm
        self.state = [False] * 4
        self.light_state = False
        self.anykey = False
        self.relay_ch = 18
        self.p1 = pcf8574_io.PCF(0x20)
        self.tested = [False] * 4
        self.testmode = False
        self.anykeymode = False

        GPIO.setup(self.relay_ch, GPIO.OUT)

    def turn_on_light(self):
        if not self.light_state:
            try:
                GPIO.output(self.relay_ch, GPIO.LOW)
                self.light_state = True
                return True
            except:
                return False

    def turn_off_light(self):
        if self.light_state:
            try:
                GPIO.output(self.relay_ch, GPIO.HIGH)
                self.light_state = False
                return True
            except:
                return False

