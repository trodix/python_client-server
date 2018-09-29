# Import socket module 
import socket 
  
  
class Client: 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 8888

    s = None

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):

        try:
            # connect to server on local computer 
            self.s.connect((self.host, self.port)) 
            print("Client connected to server {}:{}".format(self.host, self.port))

            while True: 
    
                # message you send to server 
                message = input('\n>> Command: ')

                # message sent to server 
                self.s.send(message.encode('utf-8')) 
        
                # messaga received from server 
                data = self.s.recv(1024)

                if not data:
                    print("Server lost")
                    break
        
                # print the received message 
                # here it would be a reverse of sent message 
                print("[Received from server]", str(data.decode('utf-8'))) 
        
                # ask the client whether he wants to continue 
                ans = input('\n>> Do you want to continue(y/n): ') 
                if ans == 'y': 
                    continue
                else: 
                    break

        except ConnectionError:
            print("Unable to connect {}:{}".format(self.host, self.port))

        finally:
            # close the connection 
            self.s.close()