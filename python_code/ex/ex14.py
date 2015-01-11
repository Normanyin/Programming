#!/usr/bin/python
#Filename: ex14.py
#Description: backup files

import os
import time
from sys import argv

source = argv[1]

target_dir = argv[2]

target = target_dir+time.strftime('%Y%m%d') + '.zip'

zip_command = "zip -qr '%s' '%s'" %(target, source)

if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup failed'
