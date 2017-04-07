#!/usr/bin/env python
# coding: utf-8
import socket
import time


HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024

# 创建TCP/IP套接字，顺序的、可靠的、完整的
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建UDP/IP套接字（UDP:用户数据报协议），不能保证顺序性、可靠性和完整性
# udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM:datagram(数据报)

tcp_sock.bind((HOST, PORT))
tcp_sock.listen(5)
while True:
    print 'waiting for connection...'
    cs, addr = tcp_sock.accept()
    print '...connected from:', addr
    
    while True:
        data = cs.recv(BUFSIZE)
        if not data:
            break
        cs.send('[%s] %s' % (time.ctime(), data))
        
    cs.close()
tcp_sock.close()