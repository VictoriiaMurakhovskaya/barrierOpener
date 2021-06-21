# -*- coding: utf-8 -*-

from __future__ import unicode_literals

try:
    from RPLCD.i2c import CharLCD
    from time import sleep
except:
    pass


chars_dict = {
    'Б': [0b11110, 0b10000, 0b10000, 0b11110, 0b10001, 0b10001, 0b11110, 0b00000],
    'Г': [0b11111, 0b10001, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b00000],
    'Д': [0b01111, 0b00101, 0b00101, 0b01001, 0b10001, 0b11111, 0b10001, 0b00000],
    'Ж': [0b10101, 0b10101, 0b10101, 0b11111, 0b10101, 0b10101, 0b10101, 0b00000],
    'З': [0b01110, 0b10001, 0b00001, 0b00010, 0b00001, 0b10001, 0b01110, 0b00000],
    'И': [0b10001, 0b10011, 0b10011, 0b10101, 0b11001, 0b11001, 0b10001, 0b00000],
    'Й': [0b01110, 0b00000, 0b10001, 0b10011, 0b10101, 0b11001, 0b10001, 0b00000],
    'Л': [0b00011, 0b00111, 0b00101, 0b00101, 0b01101, 0b01001, 0b11001, 0b00000],
    'П': [0b11111, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b00000],
    'У': [0b10001, 0b10001, 0b10001, 0b01010, 0b00100, 0b01000, 0b10000, 0b00000],
    'Ф': [0b00100, 0b11111, 0b10101, 0b10101, 0b11111, 0b00100, 0b00100, 0b00000],
    'Ц': [0b10010, 0b10010, 0b10010, 0b10010, 0b10010, 0b10010, 0b11111, 0b00001],
    'Ч': [0b10001, 0b10001, 0b10001, 0b01111, 0b00001, 0b00001, 0b00001, 0b00000],
    'Ш': [0b10101, 0b10101, 0b10101, 0b10101, 0b10101, 0b10101, 0b11111, 0b00000],
    'Щ': [0b10101, 0b10101, 0b10101, 0b10101, 0b10101, 0b10101, 0b11111, 0b00001],
    'Ь': [0b10000, 0b10000, 0b10000, 0b11110, 0b10001, 0b10001, 0b11110, 0b00000],
    'Ы': [0b10001, 0b10001, 0b10001, 0b11001, 0b10101, 0b10101, 0b11001, 0b00000],
    'Ю': [0b10010, 0b10101, 0b10101, 0b11101, 0b10101, 0b10101, 0b10010, 0b00000],
    'Я': [0b01111, 0b10001, 0b10001, 0b01111, 0b00101, 0b01001, 0b10001, 0b00000]}

escapes = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07']

eng_rus = {'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'Н': 'H', 'О': 'O', 'Р': 'P',
           'С': 'C', 'Т': 'T', 'Х': 'X', ' ': ' ', '!': '!', '#': '#', '=': '=', ',': ',', '.': '.', '%': '%'}

for k in range(0, 10):
    eng_rus.update({str(k): str(k)})


class Display():
    def __init__(self):
        self.lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
                      cols=20, rows=4, dotsize=8,
                      charmap='A00',
                      auto_linebreaks=True)

    def rus_test(self):
        line = 'БГДЖЗИЙЛПУФЦЧШЩЬЫЮЯ     '
        line1 = line[0:8]
        line2 = line[8:16]
        line3 = line[16:19]
        str_out = '\x00\x01\x02\x03\x04\x05\x06\x07'
        for l in [line1, line2, line3]:

            for char in enumerate(l):
                self.lcd.create_char(char[0], chars_dict[char[1]])
            self.lcd.write_string(str_out[:len(l)])
            sleep(2)
            self.lcd.clear()

        self.lcd.backlight_enabled = False

        self.lcd.close(clear=True)

    def clear(self):
        self.lcd.clear()

    def welcome_message(self):
        # Здравствуйте
        # Нажмите
        # одну из кнопок
        # ЗДУЙ
        # ЖИЮП
        for char in enumerate('ЗДУЙЖИДП'):
            self.lcd.create_char(char[0], chars_dict[char[1]])
        self.lcd.cursor_pos = (0, 4)
        self.lcd.write_string('\x00\x01PABCTB\x02\x03TE!')
        self.lcd.cursor_pos = (2, 6)
        self.lcd.write_string('HA\x04M\x05TE')
        self.lcd.cursor_pos = (3, 3)
        self.lcd.write_string('O\x06H\x02 \x05\x00 KHO\x07OK')

    def turn_off(self):
        self.lcd.clear()
        self.lcd.backlight_enabled = False
        self.lcd.close(clear=True)

    def print_rus_string(self, strings):
        """
        Печатает набор строк на экране LCD2004
        Подставляет русские символы, не более 8-ми
        :param strings: список вида [((row, col), string), ...]
        (row, col) - позиция начала строки
        string - содержание строки
        :return: True - строка выведена, False - строка не выведена
        """

        strings = list(strings)

        long_string = ''

        # начальное преобразование и проверка словаря строк для вывода
        for item in strings:
            row = item[0][0]
            col = item[0][1]
            string = item[1].upper()[:min(20, len(item[1]))]
            if row > 3 | col > 19:
                raise ValueError('Illegal position')

            # формирование одной длинной строки для проверки
            long_string += item[1]

            strings[strings.index(item)] = ((row, col), string)

        rus_letters = list(chars_dict.keys())  # строка русских символов (словарь индивидуальных символов)

        # выделение и проверка количества символов, требующих подстановки
        individual_chars = list(set([item for item in long_string.upper() if item in rus_letters]))
        if len(individual_chars) > 8:
            raise ValueError('Too many RUS symbols: {:d}'.format(len(individual_chars)))
        else:
            print('Total RUS characters: {:d}'.format(len(individual_chars)))

        # создание словаря escape - последовательностей
        for char in enumerate(individual_chars):
            self.lcd.create_char(char[0], chars_dict[char[1]])

        # создание словаря строк для печати (английские буквы + escape последовательности)
        strings_to_print = []
        for item in strings:
            row = item[0][0]
            col = item[0][1]
            string = item[1]
            string_to_print = ''
            for letter in list(string):
                if letter in individual_chars:
                    string_to_print += escapes[individual_chars.index(letter)]
                else:
                    string_to_print += eng_rus[letter]
            strings_to_print.append(((row, col), string_to_print))
        for item in strings_to_print:
            self.lcd.cursor_pos = item[0]
            self.lcd.write_string(item[1])




