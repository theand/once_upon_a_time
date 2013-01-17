from password import *
from my_exceptions import *

class User:
	def __init__(self, aList):
		self.list = aList
		self.userId = self.homeDir = self.groupName = self.passwd = self.name = ''

	def formatting(self):
		self.verify()
		self.customFormatting()
		self.basicFormatting()
		self.makeDict()

	def verify(self):
		if len(self.list) < 4:
			print self.list
			raise IncompleteInputError

	def customFormatting(self):
		raise NotImplementedError

	def basicFormatting(self):
		self.passwd  = getPasswd(self.list[2])
		self.name = self.list[3]

	def makeDict(self):
		self.dict = {'id':self.userId,
					'name':self.name,
					'group':self.groupName,
					'passwd' : self.passwd,
					'dir': self.homeDir}

	def getDict(self):
		return self.dict


class Under(User):
	def customFormatting(self):
		self.userId = 'cs'+ self.list[1]
		self.groupName = 'under'
		self.homeDir = '/home/under/'+self.userId

	def __str__(self):
		return 'Under : ID/%s , Password/%s , Name:%s' % (self.userId, self.passwd, self.name )
	
class Grad(User):
	def customFormatting(self):
		self.userId = 'gr'+ self.list[1]
		self.groupName = 'grad'
		self.homeDir = '/home/grad/'+self.userId

	def __str__(self):
		return 'Grad : ID/%s , Password/%s , Name:%s' % (self.userId, self.passwd, self.name )


class Prof(User):
	def customFormatting(self):
		self.userId = self.list[1]
		self.groupName = 'prof'
		self.homeDir = '/home/prof/'+self.userId

	def __str__(self):
		return 'Prof : ID/%s , Password/%s , Name:%s' % (self.userId, self.passwd, self.name )


class Etc(User):
	def customFormatting(self):
		self.userId = 'cs'+ self.list[1]
		self.groupName = 'etc'
		self.homeDir = '/home/etc/'+self.userId

	def __str__(self):
		return 'Etc : ID/%s , Password/%s , Name:%s' % (self.userId, self.passwd, self.name )


