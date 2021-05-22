import socket

deviceAmount = 4
gateway = ("localhost", 8200)
server = ("localhost",8000)

deviceInterface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
deviceInterface.bind(gateway)

serverInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverInterface.connect(server)

# sendMeasurements invia le letture raccolte al server.
def sendMeasurements(mes):
    serverInterface.send(mes.encode("utf-8"))
    print("Sent measurement to server!")
    
def main():
    receivedAmount=0
    total = ""
    while True:
        message = deviceInterface.recv(1024)
        receivedAmount += 1
        total = total + message.decode("utf-8")
        print("receivede measurement (%d/%d)" % (receivedAmount,deviceAmount))
        if receivedAmount == deviceAmount:
            sendMeasurements(total)
            receivedAmount = 0
            total = ""

if __name__ == "__main__":
    main()