#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 5555

class ServerProtocol(protocol.Protocol):
    
    def connectionMade(self):
        self.client = self.transport.getPeer().host
        print '...connection from ', self.client
        
    def dataReceived(self, data):
        self.transport.write('[%s] %s' % ( ctime(), data))
        
factory = protocol.Factory()
factory.protocol = ServerProtocol
print 'waiting for connection....'
reactor.listenTCP(PORT, factory)
reactor.run()