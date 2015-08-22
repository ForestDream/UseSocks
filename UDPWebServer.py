#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)

ServerSocket = socket(AF_INET, SOCK_DGRAM)
ServerSocket.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = ServerSocket.recvfrom(BUFSIZE)
    if not data:
        break
    ServerSocket.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from and returned to:', addr
    
ServerSocket.close()
