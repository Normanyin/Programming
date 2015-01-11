#!/usr/bin/python
import re

a = re.compile(r"""\d + # the integral part
				   \.   #the decimal point
				   \d * #some fractional digits""", re.X)

b = re.compile(r"\d+\.\d*")

match11 = a.match('33.1415')
match12 = a.match('33')
match21 = b.match('3.1415')
match22 = b.match('33')

if match11:
	print match11.group()
else:
	print u'match11 is not decimal'
	
if match12:
	print match12.group()
else:
	print 'match12 is not decimal'
	
if match21:
	print match21.group()
else:
	print 'match21 is not decimal'
	
if match22:
	print match22.group()
else:
	print 'match22 is not decimal'
