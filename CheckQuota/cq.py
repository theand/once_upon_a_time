#!/bin/env python

import os
import sys

if __name__=="__main__":
	#os.system("du -sk ./* > du.history")
	file = open("./du.history","r")
	if file == None:
		print "Error: Can't open history file.\n"
		sys.exit(0)
	if len(sys.argv) == 1:
		MAX_USAGE = 100000
	else:
		MAX_USAGE = int(sys.argv[1])
	lines = file.readlines()
	for each in lines:
		(usage, stdNumber) = each.split()
		if int(usage) > MAX_USAGE:
			print '%s : %.d MB' % (stdNumber, int(usage)/1000.0)

