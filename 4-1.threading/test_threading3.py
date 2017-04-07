#!/usr/bin/env python
# coding:utf-8
'''派生Thread的子类，并创建子类的实例（推荐）'''

import threading
from time import ctime, sleep

loops = [4,2]

class MyThread(threading.Thread):
    
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        
    def run(self):
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
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
        
    for i in nloops:    # start threads
        threads[i].start()
        
    for i in nloops:    # wait for all threads to finish
        threads[i].join()
        
    print 'all DONE at: ', ctime()
    
if __name__ == '__main__':
    main()