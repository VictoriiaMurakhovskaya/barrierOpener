# Модуль socketserver для сетевого программирования
from socketserver import BaseRequestHandler, TCPServer
from components.show_message import show_message

# данные сервера
host = '192.168.3.20'
port = 9091
addr = (host, port)


# обработчик запросов TCP подкласс StreamRequestHandler
class MyTCPHandler(BaseRequestHandler):

    # функция handle делает всю работу, необходимую для обслуживания запроса.
    def handle(self):
        self.data = self.request.recv(1024)
        show_message()


if __name__ == "__main__":
    # Создаем экземпляр класса
    server = TCPServer(addr, MyTCPHandler)

    print('starting server... for exit press Ctrl+C')
    # serve_forever - запускаем сервер
    server.serve_forever()
