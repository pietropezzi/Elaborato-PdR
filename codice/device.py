from datetime import datetime as dt
import time
import random
import socket

device_ip = "192.168.1.1"
gateway = ("localhost", 8200)

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

def sendMeasure(measurement):
    deviceSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    deviceSocket.connect(gateway)
    deviceSocket.send(measurement.encode("UTF-8"))
    deviceSocket.close()
    print("Measurement sent to gateaway...")
    
def main():
    # check if file exists
    while True:
        sendMeasure(measure())
        time.sleep(20)
        # sendMeasure(measure())
        # time.sleep(120)
    
if __name__ == "__main__":
    main()