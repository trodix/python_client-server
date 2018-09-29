from client import Client

def Main():
    
    cli = Client('127.0.0.1', 8888)
    cli.connect()

if __name__ == '__main__':
    Main()