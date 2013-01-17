#!/usr/bin/python

# user add script v. 05
# created by Chae Heesang. 2001. 9. 5
# updated 2001. 11. 27

# run this script daily.
# user information is located at "user.dat"

import sys, os, string, crypt, whrandom

def printUsage(scriptFilename):
	print """Usage : %s file_name

Note. user information file format
[Group_Identifier] [Student_ID] [Password] [Name] 

Group_Identifier	:	U or G or E;(Undergraduate,Graduate,Etc)
Student_ID		:	unique 6 digit id number.
Password		:	at least 6 chars
Name			:	English. White space is not allowed.

Example :
	U 991000 password ArMugae
	or
	G 001000 12345678 HongKilDong""" % scriptFilename

def getSalt():
	salt = ""
	for j in range(2):
		i = whrandom.randint(0,9)%3
		if i == 0 :
			i = (whrandom.randint(0,9)%11)
		elif i == 1:
			i = (whrandom.randint(0,9)%25)
		elif i == 2:
			i = (whrandom.randint(0,9)%25)
		salt = salt + str(i)
	return (salt)

if __name__ == "__main__" :
	if len ( sys.argv ) != 2 :
		printUsage(sys.argv[0])
		#sys.exit(1)

	try:
		#lines = open(sys.argv[1],"r").readlines()
		lines = open("user.dat","r").readlines()
	except IOError:
		print "User data file has error."
		sys.exit(1)

	if len(lines)== 0 :
		print "Data file has no entry."
		sys.exit(1)

	for i in lines :
		i = string.strip(i)
		try:	
			[group, id, password, name] = string.split(i)
		except ValueError:
			print "May be there are some error in a line : '%s' " % i
			continue

		if (len(group)!=1) or (len(id)!=6) or (len(password)<4) or (len(name)<5) :
			print "Abnormal input : " + group + id + password + name
			continue

		if string.lower(group) == "u" :
			group = "under"
			account = "cs"+id
			homeDirectory = "/home/under/"+account
		elif string.lower(group) =="g" :
			group = "grad"
			account = "gr"+id
			homeDirectory = "/home/grad/"+account
		elif string.lower(group) =="e" :
			group = "etc"
			account = "cs"+id
			homeDirectory = "/home/etc/"+account
		else :
			print "Group Identifier had wrong character :" + group + id 
			continue

		cryptedpassword = crypt.crypt(password,getSalt())

		print "Creating...userid : "+account

		statement = "useradd %s -c %s -g %s -d %s -p %s" % (account, name, group, homeDirectory, cryptedpassword)
		#os.system(statement)
		print statement
		print "------------------------------------"

	print "Finished!"
