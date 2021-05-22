import socket

server = ("localhost", 8000) 

gatewayInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gatewayInterface.bind(server)
gatewayInterface.listen(1)

connSocket, addr = gatewayInterface.accept() 

def main():	
    while True:
        message = connSocket.recv(4096)
        print(message.decode("utf-8"))

if __name__ == "__main__":
    main()
