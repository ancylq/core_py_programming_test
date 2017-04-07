#!/usr/bin/env python
# coding:utf-8

from atexit import register
from re import compile
from threading import Thread
from time import ctime
import urllib2 

REGX = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {'0132269937': 'Core Python Programing',
         '0132356139': 'Python Web Devlopment with Django',
         '0137143419': 'Python Fundamentals'}

def getRanking(isbn):
    url = '%s%s' % (AMZN, isbn)
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0')
    request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('Accept-Language', 'en-US,en;q=0.5')
    page = urllib2.urlopen(request)
    data = page.read()
    page.close()
    return REGX.findall(data)[0]

def _showRanking(isbn):
    print '- %r ranked %s' % (ISBNs[isbn], getRanking(isbn))
    
def main():
    print 'At ', ctime(), ' on Amazon ...'
    for isbn in ISBNs:
        #_showRanking(isbn)
        Thread(target=_showRanking, args=(isbn,)).start()
    
@register    # 在python解释器中注册一个退出函数，会在脚本退出之前请求调用这个特殊函数。
def _atexit():
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    main()
