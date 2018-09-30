import socket 
from threading import Thread
from datetime import datetime

import subprocess

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    ip = '127.0.0.1'
    port = 8888
    conn = None
 
    def __init__(self, conn, ip, port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        print("[+] [{}:{}] [{}] New server socket thread started".format(ip, str(port), datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
 
    def run(self): 
        while True : 
            raw = self.conn.recv(2048)

            if not raw:
                print("[-] [{}:{}] [{}] Disconnected".format(self.ip, self.port, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                break

            data = raw.decode('utf-8')
            print("[*] [{}:{}] [{}] Received data: {}".format(self.ip, self.port, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), data))

            response = self.data_process(data)

            self.conn.send(response.encode('utf-8'))

    def data_process(self, data):
        return data[::-1]

class TcpServer:

    # Multithreaded Python server : TCP Server Socket Program Stub
    TCP_IP = '' 
    TCP_PORT = 8888 
    BUFFER_SIZE = 1024  # Usually 1024, but we need quick response
    threads = []

    def __init__(self, ip, port, buffer_size):
        self.TCP_IP = ip
        self.TCP_PORT = port
        self.BUFFER_SIZE = buffer_size
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
         
        #self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.s.bind((self.TCP_IP, self.TCP_PORT)) 
 
        while True: 
            self.s.listen() 
            print("[*] [{}] Multithreaded Python server : Waiting for connections from TCP clients...".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            (cli_conn, (cli_ip, cli_port)) = self.s.accept() 
            newthread = ClientThread(cli_conn, cli_ip, cli_port) 
            newthread.start() 
            self.threads.append(newthread) 
        
        for t in self.threads: 
            t.join() 