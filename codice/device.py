from datetime import datetime as dt
import time
import random
import socket
import os 

"""
 readingsAmount -> Numero di letture da effettuare prima di inviarle
                   al gateway (Non può essere 0)
 readingsBreak  -> Intervallo di tempo tra ogni lettura. (in secondi)
"""
readingsAmount = 3
readingsBreak = 5

# Check on User given data
if readingsAmount == 0:
    print("[Err] readingsAmount needs to be greater than 0.")
    input("Press anything to close...")
    exit 
    
device_ip = "192.168.1.1"
gateway = ("localhost", 8200)  

deviceSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

def measure():
    # Time
    time = dt.now()
    strTime = time.strftime(" %H:%M:%S ")
    # Temperature
    groundTemp = str(random.randint(15, 32)) + "°C "
    # Humidity 
    humidity = str(random.randint(10, 45)) + "% "
    # Final reading
    return device_ip + " -" + strTime + groundTemp + humidity

def wipeReadings(filename):
    with open(filename, "r+") as f:
        f.truncate(0)
        f.close()
        
def sendMeasure(filename):
    m = ""
    with open(filename, "r") as f:
        for line in f.readlines():
            m = m + line
        f.close()
    deviceSocket.sendto(m.encode(), gateway)
    
def main():
    print("[#] Device "+device_ip+" Now enabled.")
    readingtxt = "Dev"+device_ip+"Read.txt"
    r = 0
    if os.path.isfile(readingtxt):
        wipeReadings(readingtxt)
    while True:
        with open(readingtxt, "a") as f:
            f.write(measure()+"\n")
            if r != readingsAmount - 1:
                f.write("\n")
            f.close()
        r += 1
        if r == readingsAmount:
            sendMeasure(readingtxt)
            r = 0
            wipeReadings(readingtxt)
            print("[+] Sent measurements to gateway.")
        time.sleep(readingsBreak)
    
if __name__ == "__main__":
    main()