import socket

deviceAmount = 4
server = ("localhost",8000)

deviceInterface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
deviceInterface.bind(("localhost", 8200))

def sendMeasurements(mes):
    serverInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverInterface.connect(server)
    serverInterface.send(mes.encode("utf-8"))
    print("Sent measurement to server!")
    serverInterface.close()
    
def main():
    receivedAmount=0
    total = ""
    while True:
        message = deviceInterface.recv(4096)
        receivedAmount += 1
        total = total + message.decode("utf-8") +"\n"
        print("receivede measurement (%d/%d)" % (receivedAmount,deviceAmount))
        if receivedAmount == deviceAmount:
            sendMeasurements(total)
            receivedAmount = 0
            total = ""

if __name__ == "__main__":
    main()