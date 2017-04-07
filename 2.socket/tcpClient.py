#!/usr/bin/env python
# coding:utf-8
import socket


HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    data = raw_input('>')
    if not data:
        break
    sock.send(data)
    server_data = sock.recv(BUFSIZE)
    if not server_data:
        break
    print server_data
    
sock.close()