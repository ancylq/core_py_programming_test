#!/usr/bin/env python
# coding:utf-8

'''创建一个Thread实例，传给它一个函数，不推荐'''

import threading
from time import ctime, sleep

loops = [4, 2]

def loop(n, sec):
    print 'start loop', n, ' at: ', ctime()
    sleep(sec)
    print 'loop', n, ' done at: ', ctime()
    
def main():
    print 'starting at: ', ctime()
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
        
    for i in nloops:    # start threads
        threads[i].start()
        
    for i in nloops:    # wait for all threads to finish
        threads[i].join()
        
    print 'all DONE at: ', ctime()
    
if __name__ == '__main__':
    main()