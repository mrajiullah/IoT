from network import LTE
import time

lte = LTE()
lte.attach(band=20, apn="lpwa.telia.iot")
while not lte.isattached():
    time.sleep(0.25)
lte.connect()       # start a data session and obtain an IP address
while not lte.isconnected():
    time.sleep(0.25)
