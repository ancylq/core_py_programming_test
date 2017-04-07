#!/usr/bin/env python
# coding:utf-8
from twisted.internet import protocol, reactor

HOST = '127.0.0.1'
PORT = 5555

class ClientProtocol(protocol.Protocol):
    
    def sendData(self):
        data = raw_input('> ')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()
            
    def connectionMade(self):
        self.sendData()
        
    def dataReceived(self, data):
        print 'received data...', data
        self.sendData()
        
class ClientFactory(protocol.ClientFactory):
    protocol = ClientProtocol
    clientConnectionLost = clientConnectionFaild = lambda self, connector, reason:reactor.stop()
    
reactor.connectTCP(HOST, PORT, ClientFactory())
reactor.run()