#!/usr/bin/python

import re

CODEC = 'unicode'

sourcefile = "testfile"
targetfile = "jspfile"


def get_jspfile_list():
	
f = open(sourcefile)
t = open(targetfile)
targettext = t.read()
t.close()
t = open(targetfile,'w')
for line in f.readlines():
    name = line.split("=")
    targetname = name[0]
    sourcename = name[1].decode('unicode_escape').encode('utf-8')
    pattern = re.compile(r'<s:text name=[\"\']'+targetname+r'[\"\'].*?>{1}')
    for result in pattern.finditer(targettext):
    	targettext = targettext.replace(result.group(),sourcename.strip('\r\n'))
t.write(targettext)
f.close()
t.close()
