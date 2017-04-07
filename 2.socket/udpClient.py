#!/usr/bin/env python
# coding:utf-8


import socket

HOST = '127.0.0.1'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udp_sock.sendto(data, ADDR)
    server_data, addr = udp_sock.recvfrom(BUFSIZE)
    if not server_data:
        break
    print server_data
    
udp_sock.close()