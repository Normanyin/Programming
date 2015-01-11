#!/usr/bin/python
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print arg1,'is the first'

def print_none():
	print "I got nothing"

print_two("Abc","def")
print_two_again("Abc","def")
print_one("First")
print_none()
