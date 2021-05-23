import socket
import sys

deviceAmount = 4
gateway = ("localhost", 8200)
server = ("localhost",8000)

deviceInterface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
deviceInterface.bind(gateway)

serverInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serverInterface.connect(server)
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
    receivedAmount=0
    total = ""
    while True:
        try:
            message = deviceInterface.recv(1024)
        except Exception as e:
            print("Errore ricezione messaggio da un device.")
            print("Err: "+e)
            sys.exit(1)
        receivedAmount += 1
        total = total + message.decode("utf-8")
        print("receivede measurement (%d/%d)" % (receivedAmount,deviceAmount))
        if receivedAmount == deviceAmount:
            sendMeasurements(total)
            receivedAmount = 0
            total = ""

if __name__ == "__main__":
    main()