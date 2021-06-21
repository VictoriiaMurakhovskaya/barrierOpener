from unittest import TestCase, main
from lcd import Display

class TestSubStr(TestCase):
    def test1(self):
        lcd = Display()
        lcd.print_rus_string(1, 1, 'Здравствуйте')

if __name__ == '__main__':
    main()