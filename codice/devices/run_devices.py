import device
import time
from threading import Thread

def rundevices():
    td1 = Thread(target=device.create, args=("192.168.0.1", "D01", 3, 7))
    td1.start()
    time.sleep(1)
    td2 = Thread(target=device.create, args=("192.168.0.2", "D02", 3, 7))
    td2.start()
    time.sleep(1)
    td3 = Thread(target=device.create, args=("192.168.0.3", "D03", 3, 7))
    td3.start()
    time.sleep(1)
    td4 = Thread(target=device.create, args=("192.168.0.4", "D04", 3, 7))
    td4.start()

if __name__ == "__main__":
    rundevices()