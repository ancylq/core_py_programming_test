#!/usr/bin/env python
# coding:utf-8

from time import ctime, sleep
import thread

def loop0():
    print 'start loop 0 :', ctime()
    sleep(4)
    print 'loop 0 end:', ctime()
    
def loop1():
    print 'start loop 1 :', ctime()
    sleep(2)
    print 'loop 1 end:', ctime()
    
def main():
    print 'staring at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    main()