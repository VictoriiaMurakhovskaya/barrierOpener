import smbus as smbus
from subprocess import *
import RPIO

RPIO.setup(25, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)