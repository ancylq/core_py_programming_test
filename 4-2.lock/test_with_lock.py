#!/usr/bin/env python
# coding:utf-8

from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock # -----多的
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)
    
lock = Lock() # -----多的
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(sec):
    myname = currentThread().name
    lock.acquire() # -----多的
    remaining.add(myname)
    print '[%s] Started %s' % (ctime(), myname)
    lock.release() # -----多的
    sleep(sec)
    lock.acquire() # -----多的
    remaining.remove(myname)
    print '[%s] Completed %s (%d secs)' % (ctime(), myname, sec)
    print '    (remaining: %s)' % ( remaining or 'None')
    lock.release() # -----多的
    
def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
        
@register
def _atexit():
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    _main()
    '''正常输出
[Fri Jul 22 15:22:20 2016] Started Thread-1
[Fri Jul 22 15:22:20 2016] Started Thread-2
[Fri Jul 22 15:22:20 2016] Started Thread-3
[Fri Jul 22 15:22:20 2016] Started Thread-4
[Fri Jul 22 15:22:20 2016] Started Thread-5
[Fri Jul 22 15:22:22 2016] Completed Thread-1 (2 secs)
    (remaining: Thread-5, Thread-4, Thread-3, Thread-2)
[Fri Jul 22 15:22:22 2016] Completed Thread-2 (2 secs)
    (remaining: Thread-5, Thread-4, Thread-3)
[Fri Jul 22 15:22:22 2016] Completed Thread-4 (2 secs)
    (remaining: Thread-5, Thread-3)
[Fri Jul 22 15:22:23 2016] Completed Thread-3 (3 secs)
    (remaining: Thread-5)
[Fri Jul 22 15:22:24 2016] Completed Thread-5 (4 secs)
    (remaining: None)
all DONE at: Fri Jul 22 15:22:24 2016
'''