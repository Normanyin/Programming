#!/usr/bin/python

import string, urllib2

def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page + 1):
        sName = string.zfill(i, 5) + '.html'
        print 'downloading ' + str(i) +' page, and save as ' + sName + '.......'
        f = open(sName, 'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

bdurl = 'http://tieba.baidu.com/p/2296017831?pn='
begin_page = 1
end_page = 10

baidu_tieba(bdurl, begin_page, end_page)
