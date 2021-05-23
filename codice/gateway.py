import socket
import sys

deviceAmount = 4
gateway = ("localhost", 8200)
server = ("localhost",8000)

deviceInterface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
deviceInterface.bind(gateway)

serverInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("Connessione con server...")
    serverInterface.connect(server)
    print("Connessione con server stabilita.")
except Exception as e:
    print("Errore durante connessione con server.")
    print("Err: "+e)
    sys.exit(1)

# sendMeasurements invia le letture raccolte al server.
def sendMeasurements(mes):
    try:
        serverInterface.send(mes.encode("utf-8"))
        print("Sent measurement to server!")
    except Exception as e:
        print("Errore duranto invio letture al server.")
        print("Err: "+e)
        input()
        sys.exit(1)
        
def main():
    devReceived = []
    receivedAmount=0
    total = ""
    while True:
        try:
            message = deviceInterface.recv(1024)
        except Exception as e:
            print("Errore ricezione messaggio da un device.")
            print("Err: "+e)
            sys.exit(1)
        decmess = message.decode("utf-8")
        devip = decmess[0:11]
        if devip in list(devReceived):
            print("lettura device "+devip+" già ottenuta, messaggio scartato.")
        else:
            devReceived.append(devip)
            receivedAmount += 1
            total = total + decmess
            print("receivede measurement (%d/%d)" % (receivedAmount,deviceAmount))
            if receivedAmount == deviceAmount:
                sendMeasurements(total)
                receivedAmount = 0
                devReceived = []
                total = ""

if __name__ == "__main__":
    main()