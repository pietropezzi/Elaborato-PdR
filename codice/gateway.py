import socket
import sys

deviceAmount = 4
gateway = ("localhost", 8200)
server = ("localhost",8000)

# creazione socket UDP per i device.
deviceInterface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
deviceInterface.bind(gateway)

# creazione sockect TPC per server.
serverInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connessione con server.
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
        print("Misure inviate al server.")
    except Exception as e:
        print("Errore duranto invio letture al server.")
        print("Err: "+e)
        input()
        sys.exit(1)
        
def main():
    # ip dei dispositivi ricevuti.
    devReceived = []
    # num di messaggi ricevuti da dispositivi.
    receivedAmount=0
    total = ""
    while True:
        try:
            message = deviceInterface.recv(1024)
        except Exception as e:
            print("Errore ricezione messaggio da un device.")
            print("Err: "+e)
            sys.exit(1)
        # controllo se ho gia ricevuto un messaggio da questo ip.
        decmess = message.decode("utf-8")
        devip = decmess[0:11]
        if devip in list(devReceived):
            # se ho gia ricevuto questo messaggio lo scarto
            print("lettura device "+devip+" già ottenuta, messaggio scartato.")
        else:
            # altrimenti incremento il contatore di received amount
            # e aggiungo l'ip alla lista dei ricevuti.
            devReceived.append(devip)
            receivedAmount += 1
            total = total + decmess
            print("Messaggio ricevuto, devcount: (%d/%d)" % (receivedAmount,deviceAmount))
            # controllo se ho ricevuto tutti i dispositivi, se si
            # invio le letture ottenute al server.
            if receivedAmount == deviceAmount:
                sendMeasurements(total)
                receivedAmount = 0
                devReceived = []
                total = ""

if __name__ == "__main__":
    main()
