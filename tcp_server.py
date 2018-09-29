import socket
from _thread import *
import threading

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
            print("[{}:{} - Connected]".format(addr[0], addr[1]))
    
            # Start a new thread and return its identifier 
            start_new_thread(self.threaded, (c, addr)) 
        s.close()

    def threaded(self, c, addr):
        while True:
            data = c.recv(1024)

            if not data:
                print("[{}:{} - Disconnected]".format(addr[0], addr[1]))
                self.print_lock.release()
                break

            print("[{}:{} - Received Data from client] {}".format(addr[0], addr[1], data))
            data = data[::-1]

            c.send(data)

        c.close()