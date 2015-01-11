#!/usr/bin/python
#Filename: exd09.py

number = 22
running = True
while running:
	guess = int(raw_input('Enter an integer:'))

	if guess == number:
		print 'Congratulations'
		running = False
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, is is a little lower than that'
else:
	print 'The while loop is over.'

print 'Done'
