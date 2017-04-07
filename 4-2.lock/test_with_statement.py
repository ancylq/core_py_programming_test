#!/usr/bin/env python
# coding:utf-8

from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(sec):
    myname = currentThread().name
    with lock:
        remaining.add(myname)
        print '[%s] Started %s' % (ctime(), myname)
    sleep(sec)
    with lock:
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
'''
[Fri Jul 22 15:29:29 2016] Started Thread-1
[Fri Jul 22 15:29:29 2016] Started Thread-2
[Fri Jul 22 15:29:29 2016] Started Thread-3
[Fri Jul 22 15:29:29 2016] Started Thread-4
[Fri Jul 22 15:29:29 2016] Started Thread-5
[Fri Jul 22 15:29:31 2016] Completed Thread-3 (2 secs)
    (remaining: Thread-5, Thread-4, Thread-2, Thread-1)
[Fri Jul 22 15:29:31 2016] Completed Thread-4 (2 secs)
    (remaining: Thread-5, Thread-2, Thread-1)
[Fri Jul 22 15:29:32 2016] Completed Thread-2 (3 secs)
    (remaining: Thread-5, Thread-1)
[Fri Jul 22 15:29:32 2016] Completed Thread-5 (3 secs)
    (remaining: Thread-1)
[Fri Jul 22 15:29:33 2016] Completed Thread-1 (4 secs)
    (remaining: None)
all DONE at: Fri Jul 22 15:29:33 2016
'''