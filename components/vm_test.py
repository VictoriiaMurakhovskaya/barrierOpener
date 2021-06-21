from vending import Machine
from time import sleep

if __name__ == '__main__':
    vm = Machine()
    vm.display.print_rus_string((((0, 2), 'Тест компонентов'),
                                 ((2, 4), 'Любая кнопка'),
                                 ((3, 2), 'для продолжения')))
    vm.wait_any_key()
    vm.buttons.turn_on_light()
    #vm.buttons.run_key_test()
    vm.display.clear()
    t1t2 = vm.t.get_temperature()
    vm.display.print_rus_string((((0, 4), 'Температура'),
                                 ((1, 2), 'Датчик 1 Т={:.2f}'.format(t1t2[1])),
                                 ((2, 2), 'Датчик 2 Т={:.2f}'.format(t1t2[2]))))
    vm.wait_any_key()
    vm.display.clear()
    h1h2 = vm.t.get_humidity()
    vm.display.print_rus_string((((0, 5), 'Влажность'),
                                 ((1, 1), 'Датчик 1 Н={:.2f}%'.format(h1h2[1])),
                                 ((2, 1), 'Датчик 2 Н={:.2f}%'.format(h1h2[2]))))
    vm.wait_any_key()
    vm.display.clear()
    vm.display.print_rus_string((((1, 4), 'Тестирование'),
                                 ((2, 6), 'окончено')))
    sleep(2)
    vm.buttons.turn_off_light()
    vm.display.turn_off()