import socket

gatewayInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gatewayInterface.bind(("localhost",8000))
gatewayInterface.listen(1)

def main():	
    while True:
        connSocket, addr = gatewayInterface.accept()
        message = connSocket.recv(4096)
        print(message.decode("utf-8"))
        connSocket.close()

if __name__ == "__main__":
    main()
