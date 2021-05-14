import socket

server = ("localhost",8000)

deviceInterface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
deviceInterface.bind(("localhost", 8200))

def sendMeasurements(mes):
    serverInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverInterface.connect(server)
    serverInterface.send(mes)
    serverInterface.close()
    
while True:
    message = deviceInterface.recv(1024)
    print("received message from someone")
    sendMeasurements(message)