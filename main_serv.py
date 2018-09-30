from tcp_server import TcpServer

def Main():
    serv = TcpServer('', 8888, 1024)
    serv.start()

if __name__ == '__main__':
    Main()