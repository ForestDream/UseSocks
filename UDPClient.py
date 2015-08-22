#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)

Socket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    Socket.sendto(data, ADDR)
    data, ADDR = Socket.recvfrom(BUFSIZE)
    if not data:
        break
    print data
    
Socket.close()
