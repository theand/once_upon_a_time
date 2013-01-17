#!/usr/bin/env python

import scanner
import machine
from my_exceptions import *
import os
	


if __name__ == "__main__":
	try:
		sc = scanner.Scanner(open("user.dat"))
	except IOError:
		import sys
		print "user.dat doesn't exist"
		sys.exit(1)

	sc.main()

	for i in sc.getObjList():
		try:
			machine.addUser(i)
		except AlreadyExistingUser:
			machine.setUserPassword(i)
	os.chdir('/var/yp')
	os.system('make')
	os.chdir('/root')

