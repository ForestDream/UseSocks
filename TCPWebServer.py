#!/usr/bin/env python
from socket import *
from time import ctime

HOST = ''
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)

ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.bind(ADDR)
ServerSocket.listen(5)

while True:
    print 'waiting for connection...'
    ConnectionSocket, addr = ServerSocket.accept()
    print '...connected from:', addr
    
    while True:
        data = ConnectionSocket.recv(BUFSIZE)
        if not data:
            break
        ConnectionSocket.send('[%s] %s' % (ctime(), data))
    ConnectionSocket.close()
ServerSocket.close()
