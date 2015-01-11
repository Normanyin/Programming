#!/usr/bin/python

#from urllib2 import Request, urlopen
import urllib2
import cookielib

cookie = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response = opener.open('http://www.baidu.com')

for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
    
old_url = 'http://rrurl.cn/b1UZuP'
req = urllib2.Request(old_url)
response1 = urllib2.urlopen('http://rrurl.cn/b1UZuP')
print 'response1:', response1
#req.add_header('User-Agent', 'fake-client')
try:
    print req
    response = urllib2.urlopen(req)
    print response.info()
    print '-------------'
    print response.geturl()
    
except urllib2.HTTPError, e:
    print e.code
