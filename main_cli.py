from client import Client

def Main():
    
    cli = Client('192.168.1.14', 8888)
    cli.connect()

if __name__ == '__main__':
    Main()