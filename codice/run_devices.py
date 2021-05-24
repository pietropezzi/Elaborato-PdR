import device
import time
from threading import Thread
import sys

# Intervalli di tempo tra l'attivazione di ogni device (in secondi)
timeInt = 0.5
# Numero di letture da effettuare prima di comunicarle al gateway.
readAmount = 4
# Intervallo di tempo tra ogni lettura (in secondi)
readBreak = 5
# Numero di device che verranno attivati.
# Per ogni device deve essere generato un thread.
deviceAmount = 4

def checkvalues():
    if readAmount * 34 > 1024 or readAmount * 34 * deviceAmount > 4096:
        print("I valori inseriti non sono validi")
        sys.exit(1)
        
def rundevices():
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
