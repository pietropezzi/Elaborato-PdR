from datetime import datetime as dt
import time
import random
import socket
import os 
import sys

# socket e gateway sono gli stessi per ogni device
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
gateway = ("localhost", 10000)
   
class Device:
    # inizializzazione di un object Device.
    def __init__(self, device_ip, device_ID, readAmount, readBreak):
        self.device_ip = device_ip
        self.device_ID = device_ID
        self.readAmount = readAmount
        self.readBreak = readBreak
        self.main()
        
    # measure si occupa di generare una lettura del terreno.
    def measure(self):
        t = dt.now()
        strTime = t.strftime(" %H:%M:%S ")
        groundTemp = str(random.randint(15, 32)) + "°C "
        humidity = str(random.randint(10, 45)) + "% "
        return self.device_ip + " -" + strTime + groundTemp + humidity
    
    # wipeReadings elimina tutte le letture presenti nel reading txt.
    def wipeReadings(self, filename):
        with open(filename, "r+") as f:
            f.truncate(0)
            f.close()
   
    # sendMeasure invia le misure precedentemente effettuate al gateway.
    def sendMeasure(self, filename):
        m = ""
        with open(filename, "r") as f:
            for line in f.readlines():
                m = m + line
            f.close()
        socket.sendto(m.encode(), gateway)

    # main è il corpo principale di un Device, genera il readfile txt ed
    # effettua e invia reading utilizzando le precedenti funzioni.
    def main(self):
        readingtxt = "reads/read_"+self.device_ID+".txt"
        r = 0
        if os.path.isdir("reads") == False:
           os.mkdir("reads")
        if os.path.isfile(readingtxt):
            self.wipeReadings(readingtxt)
        while True:
            with open(readingtxt, "a") as f:
                f.write(self.measure()+"\n")
                f.close()
            r += 1
            if r == self.readAmount:
                self.sendMeasure(readingtxt)
                print("["+self.device_ID+"] letture inviate al gateway.")
                r = 0
                self.wipeReadings(readingtxt)
            time.sleep(self.readBreak)

# create crea un oggetto Device con i dati attributi.
def create(dIp, dId, rA, rB):
    Device(dIp, dId, rA, rB)
