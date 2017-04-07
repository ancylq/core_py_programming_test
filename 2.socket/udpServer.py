#!/usr/bin/env python
# coding:utf-8
import time
import socket

HOST = '127.0.0.1'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udp_sock.recvfrom(BUFSIZE)
    udp_sock.sendto('[%s] %s' % (time.ctime(), data), addr)
    print '...received from and returned to:', addr
    
udp_sock.close()