from datetime import datetime as dt
import time
import random
import socket
import os 
    
class Device:
    def __init__(self, device_ip, device_ID, readAmount, readBreak):
        self.device_ip = device_ip
        self.device_ID = device_ID
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.gateway = ("localhost", 8200)
        self.readAmount = readAmount
        self.readBreak = readBreak
        self.main()
        
    def measure(self):
        time = dt.now()
        strTime = time.strftime(" %H:%M:%S ")
        groundTemp = str(random.randint(15, 32)) + "°C "
        humidity = str(random.randint(10, 45)) + "% "
        return self.device_ip + " -" + strTime + groundTemp + humidity
    
    def wipeReadings(self, filename):
        with open(filename, "r+") as f:
            f.truncate(0)
            f.close()
   
    def sendMeasure(self, filename):
        m = ""
        with open(filename, "r") as f:
            for line in f.readlines():
                m = m + line
            f.close()
        self.socket.sendto(m.encode(), self.gateway)

    def main(self):
        readingtxt = "read_"+self.device_ID+".txt"
        r = 0
        if os.path.isfile(readingtxt):
            self.wipeReadings(readingtxt)
        while True:
            with open(readingtxt, "a") as f:
                f.write(self.measure()+"\n")
                f.close()
            r += 1
            if r == self.readAmount:
                self.sendMeasure(readingtxt)
                print("Sent reading to gateway.")
                r = 0
                self.wipeReadings(readingtxt)
            time.sleep(self.readBreak)

def create(dIp, dId, rA, rB):
    Device(dIp, dId, rA, rB)