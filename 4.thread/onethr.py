#!/usr/bin/env python
# coding:utf-8

import time

def loop0():
    print 'start loop 0 :', time.ctime()
    time.sleep(4)
    print 'loop 0 end:', time.ctime()
    
def loop1():
    print 'start loop 1 :', time.ctime()
    time.sleep(2)
    print 'loop 1 end:', time.ctime()
    
def main():
    '''模拟单进程'''
    print 'staring at:', time.ctime()
    loop0()
    loop1()
    print 'all DONE at:', time.ctime()
    
if __name__ == '__main__':
    main()