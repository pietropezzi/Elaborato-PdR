import device
import time
from threading import Thread
import sys

# Intervallo di tempo tra l'attivazione di ogni device (in secondi).
timeInt = 0.5
# Numero di letture da effettuare prima di comunicarle al gateway.
readAmount = 3
# Intervallo di tempo tra ogni lettura (in secondi).
readBreak = 2
# Numero di device che verranno attivati.
# Assicurarsi che deviceAmount corrisponda al deviceAmount di gateway!
# Per ogni device deve essere generato un thread.
deviceAmount = 4

# checkvalues controlla che i valori di readAmount e deviceAmount
# rispettino le condizioni necessarie per i buffer del gateway e del server.
def checkvalues():
    if readAmount * 34 > 1024 or readAmount * 34 * deviceAmount > 4096:
        print("I valori inseriti non sono validi")
        sys.exit(1)

# rundevices genera un thread per ogni device.
def rundevices():
    # devono essere generati deviceAmount thread, per ogni device inserire
    # <nome_thread_device> = Thread(target=device.create, args=(IP, ID, readAmount, readBreak),daemon = True)
    # <nome_thread_device>.start()
    # time.sleep(timeInt)
    td1 = Thread(target=device.create, args=("192.168.0.1", "D01", readAmount, readBreak),
                 daemon = True)
    td1.start()
    time.sleep(timeInt)
    td2 = Thread(target=device.create, args=("192.168.0.2", "D02", readAmount, readBreak),
                 daemon = True)
    td2.start()
    time.sleep(timeInt)
    td3 = Thread(target=device.create, args=("192.168.0.3", "D03", readAmount, readBreak),
                 daemon = True)
    td3.start()
    time.sleep(timeInt)
    td4 = Thread(target=device.create, args=("192.168.0.4", "D04", readAmount, readBreak),
                 daemon = True)
    td4.start()
    print("Premere ENTER per chiudere run_devices e terminare tutti i thread")
    input()
    sys.exit(0)
    
if __name__ == "__main__":
    checkvalues()
    rundevices()
