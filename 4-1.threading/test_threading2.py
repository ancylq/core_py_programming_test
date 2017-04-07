#!/usr/bin/env python
# coding:utf-8
'''创建Thread的实例，传给它一个可调用的类实例（不推荐）'''

import threading
from time import ctime, sleep

loops = [4,2]

class ThreadFunc(object):
    
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
        
    def __call__(self):
        self.func(*self.args)
        
def loop(n, sec):
    print 'start loop', n, ' at: ', ctime()
    sleep(sec)
    print 'loop', n, ' done at: ', ctime()
    
def main():
    print 'starting at: ', ctime()
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__)) # 会调用__call__()
        threads.append(t)
        
    for i in nloops:    # start threads
        threads[i].start()
        
    for i in nloops:    # wait for all threads to finish
        threads[i].join()
        
    print 'all DONE at: ', ctime()
    
if __name__ == '__main__':
    main()