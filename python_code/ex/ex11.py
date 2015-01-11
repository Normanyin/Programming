#!/usr/bin/python
#Filename: ex11.py

import ex01
def func(a, b = 5, c = 10):
	'''this is help page
aaaaaaaa'''
	print 'a is', a, 'and b is', b, 'and c is', c

func(3,7)
func(3)
func(c = 40, a = 1)
print func(c = 40, a = 1)
print func.__doc__
help(func)
