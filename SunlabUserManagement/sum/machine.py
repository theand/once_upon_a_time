import os
import commands
from my_exceptions import *



def addUser(anUser):
	statement = 'useradd %(id)s -c %(name)s -g %(group)s -d %(dir)s -p %(passwd)s' % anUser.getDict()
	#print statement
	print 'Adding User ... %(id)s' % anUser.getDict()
	output = commands.getoutput(statement)
	if output <> '':
		raise AlreadyExistingUser

def setUserPassword(anUser):
	print 'Already Existing User. so you need set user %(id)s\'s password' % anUser.getDict()
	answer = raw_input("Do you want to do that?(input y)")
	if answer == 'y':
		os.system('passwd %(id)s' % anUser.getDict()	)
	else:
		pass



