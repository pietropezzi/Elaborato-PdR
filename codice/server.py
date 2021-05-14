import socket

gatewayInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gatewayInterface.bind(("localhost",8000))
gatewayInterface.listen(1)

while True:
    connSocket, addr = gatewayInterface.accept()
    message = connSocket.recv(1024)
    print(message.decode("utf-8"))
    connSocket.close()