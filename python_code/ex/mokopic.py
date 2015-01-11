#!/usr/bin/python
#-*- coding:utf-8 -*-


import urllib
import re
import os


#IMG_REG = re.compile('<img[^>]*?src[^>]*?=[\"\'][^"]*?[\'\"]')
IMG_REG = re.compile('<img[^>]*?src2=[\"\'][^"]*?[\'\"]')
URL_REG = re.compile('<a href=".*?" title=".*?" hidefocus="true" class="nickname" target="_blank">')
LOCAL_DIR = '/usr/picture/'

def cbk(a, b, c):
	per = 100 * a * b / cpyth
	if per > 100:
		per = 100
	print '%.2f%%' % per
    
def getPictrueFromOnePage(url, dirPath):
	file = urllib.urlopen(url)
	content = file.read()
	for match in IMG_REG.findall(content):
		imgurl = match[match.index("http"):][:-1]
		filename = imgurl[imgurl.rindex("/") + 1:]
		print imgurl
		print filename
		local = dirPath + filename
		urllib.urlretrieve(imgurl, local, cbk)
        
def mainPorcess(url):
	content = urllib.urlopen(url).read()
	i = 0
	for matched in URL_REG.findall(content):
		i = i + 1
		subUrl = 'http://www.moko.cc' + matched
		print subUrl
		path = LOCAL_DIR + matched.decode('utf-8') + '\\'
		print 'path:'+path
		if not os.path.isdir(path):
			try:
				os.mkdir(path)
			except Exception as e:
				path = LOCAL_DIR + str(i) + '\\'
		print path
		getPictrueFromOnePage(subUrl, path)
		
mainPorcess('http://user.qzone.qq.com/1072849730')
