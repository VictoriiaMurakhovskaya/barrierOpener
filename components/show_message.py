from components.vending import Machine
from time import sleep


def show_message():
    vm = Machine()
    vm.buttons.turn_on_light()
    vm.display.clear()

    vm.display.print_rus_string((((3, 7), 'Открыт'),
                                 ((1, 6), 'шлагбаум')))

    sleep(3)

    vm.display.clear()
    vm.display.turn_off()
    vm.buttons.turn_off_light()


if __name__ == '__main__':
    show_message()