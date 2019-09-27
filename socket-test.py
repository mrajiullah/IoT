from network import LTE
#from socket import *

import socket
import ssl
import time
import sys
import pycom


host='google.com'
port=443
addr=(host,port)


lte = LTE()
lte.attach(band=20, apn="lpwa.telia.iot")
while not lte.isattached():
    time.sleep(0.25)
lte.connect()       # start a data session and obtain an IP address
while not lte.isconnected():
    time.sleep(0.25)
print('Connected to LTE')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
s.settimeout(5.0)

s.connect(socket.getaddrinfo(addr, port)[0][-1])
print('Socket Bind Complete....moving to send data  ')
