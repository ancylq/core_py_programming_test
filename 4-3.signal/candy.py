#!/usr/bin/env python
# coding:utf-8
'''
模拟一个简化的糖果机，该机器只有5各槽用来保持库存（糖果）。如果所有的槽都满了，糖果就
不能在家到这个既其中了；如果5个槽都空了，想要购买的消费者就无法买到糖果了。
'''
from atexit import register
from random import randrange
from threading import Thread, BoundedSemaphore, Lock
from time import sleep, ctime


lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print 'Refilling candy ...'
    try:
        candytray.release()
    except ValueError:
        print 'full, skipping'
    else:
        print 'ok'
    lock.release()
    
def buy():
    lock.acquire()
    print 'Buying candy ...'
    if candytray.acquire(False):
        print 'ok'
    else:
        print 'empty, skipping'
    lock.release()
    
def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))
        
def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))
        
def _main():
    print 'starting at:', ctime()
    nloops = randrange(2, 6)
    print 'THE CANDY MACHINE ( full weith %d bars )!' % MAX
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start() # buyer
    Thread(target=producer, args=(nloops,)).start() # vndr
    
@register
def _atexit():
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    _main()