#!/usr/bin/env python
# coding:utf-8

from HTMLParser import HTMLParser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders

URLs = ('http://python.org',
        'http://www.baidu.com')

def output(x):
    print '\n'.join(sorted(set(x)))
    
def simpleBS(url, f):
    '''use BeautifulSoup to parse all tags to get anchors
    效率不高，只用BeautifulSoup解析文档中的所有标签，接着找到锚
    '''
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))
    
def fasterBS(url, f):
    '''use BeautifulSoup to parse only anchors tags
    使用SoupStrainer辅助来来进行过滤，只处理含有锚的标签，并忽略剩余的标签，节省
    时间和内存
    '''
    output(urljoin(url, x['href']) for x in BeautifulSoup(f,
                                                         parseOnlyThese=SoupStrainer('a')))
    
def htmlparser(url, f):
    '''use HTMLParser to parser anchor tags'''
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)
    
def html5libparse(url, f):
    '''use html5lib to parse anchor tags'''
    output(urljoin(url, x.attributes['href']) \
           for x in parse(f) \
           if isinstance(x, treebuilders.default_etree.Element()) \
           and x.name == 'a')
    
def process(url, data):
    print '\n*** simple BS'
    simpleBS(url, data)
    data.seek(0)
    print '\n*** faster BS'
    fasterBS(url, data)
    data.seek(0)
    print '\n*** HTMLParser'
    htmlparser(url, data)
    data.seek(0)
    print '\n*** HTML5lib'
    html5libparse(url, data)
    
def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read()) # 将数据存入 StringIO 对象中
        f.close()
        process(url, data)
        
if __name__ == '__main__':
    main()