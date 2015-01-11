#!/usr/bin/python

import re

pattern = re.compile(r'hello')

match1 = pattern.match('hello worldhello!')
match2 = pattern.match('helloo worldhello!')
match3 = pattern.match('helllo world!')

if match1:
	matchssss = pattern.findall('hello worldhellohello!')
	print matchssss[0]+matchssss[1]
	for match in matchssss:
		print len(match)
else:
	print 'match1 failed'
	
if match2:
	print match2.group()
else:
	print 'match2 failed'
	
if match3:
	print match3.group()
else:
	print 'match3 failed'
	
