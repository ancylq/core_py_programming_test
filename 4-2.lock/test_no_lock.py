#!/usr/bin/env python
# coding:utf-8

from atexit import register
from random import randrange
from threading import Thread, currentThread
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)
    
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(sec):
    myname = currentThread().name
    remaining.add(myname)
    print '[%s] Started %s' % (ctime(), myname)
    sleep(sec)
    remaining.remove(myname)
    print '[%s] Completed %s (%d secs)' % (ctime(), myname, sec)
    print '    (remaining: %s)' % ( remaining or 'None')
    
def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
        
@register
def _atexit():
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    _main()
    '''会有奇怪的输出
[Fri Jul 22 15:14:01 2016] Started Thread-1
[Fri Jul 22 15:14:01 2016] Started Thread-2
[Fri Jul 22 15:14:01 2016] Started Thread-3
[Fri Jul 22 15:14:01 2016] Started Thread-4
[Fri Jul 22 15:14:01 2016] Started Thread-5
[Fri Jul 22 15:14:01 2016] Started Thread-6
[Fri Jul 22 15:14:03 2016] Completed Thread-4 (2 secs)
    (remaining: Thread-6, Thread-5, Thread-3, Thread-2, Thread-1)
[Fri Jul 22 15:14:04 2016] Completed Thread-1 (3 secs)
    (remaining: Thread-6, Thread-5, Thread-3, Thread-2)
[Fri Jul 22 15:14:04 2016] Completed Thread-5 (3 secs)
    (remaining: Thread-6, Thread-3, Thread-2)
[Fri Jul 22 15:14:05 2016] Completed Thread-2 (4 secs)
 [Fri Jul 22 15:14:05 2016] Completed Thread-6 (4 secs)
    (remaining: None)
[Fri Jul 22 15:14:05 2016] Completed Thread-3 (4 secs)
    (remaining: None)
    (remaining: None)
all DONE at: Fri Jul 22 15:14:05 2016
'''