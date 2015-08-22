#!/usr/bin/env python
from socket import *

HOST = 'localhost'
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)

Socket = socket(AF_INET, SOCK_STREAM)
Socket.connect(ADDR)


while True:
    data = raw_input('> ')
    if not data:
        break
    Socket.send(data)
    data = Socket.recv(BUFSIZE)
    if not data:
        break
    print data
Socket.close()
