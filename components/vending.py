from components.buttons import Buttons
from components.lcd import Display
import RPi.GPIO as GPIO


class Machine:
    def __init__(self):

        # инициализация GPIO
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)

        # инициализация устройств
        self.display = Display()
        self.buttons = Buttons(self)

    def buttons_light_on(self):
        self.buttons.turn_on_light()

    def buttons_light_off(self):
        self.buttons.turn_off_light()

    def wait_any_key(self):
        self.buttons.wait_any_key()

