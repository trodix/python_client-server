import socket
from _thread import *
import threading
from datetime import datetime

class TcpServer:

    host = ""
    port = None
    print_lock = None

    def __init__(self, port):
        self.port = port
        self.print_lock = threading.Lock()
        

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        print('socket binded to port', self.port)

        s.listen()
        print("socket is listening")

        while True: 
   
            c, addr = s.accept() 
    
            # lock acquired by client 
            self.print_lock.acquire() 
            print("[{}] [{}:{}] [Connected]".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), addr[0], addr[1]))
    
            # Start a new thread and return its identifier 
            start_new_thread(self.threaded, (c, addr)) 
        s.close()

    def threaded(self, c, addr):
        while True:
            raw = c.recv(1024)

            if not raw:
                print("[{}] [{}:{}] [Disconnected]".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), addr[0], addr[1]))
                self.print_lock.release()
                break

            data = raw.decode('utf-8')
            print("[{}] [{}:{}] [Received Data] {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), addr[0], addr[1], data))

            response = self.data_treatment(data)
            c.send(response.encode('utf-8'))

        c.close()

    def data_treatment(self, data):
        return str(len(data))