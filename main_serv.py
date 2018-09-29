from tcp_server import TcpServer

def Main():
    serv = TcpServer(8888)
    serv.run()

if __name__ == '__main__':
    Main()