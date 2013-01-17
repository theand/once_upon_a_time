from my_exceptions import *
from user import *



def UserFactory(aList):
	if aList[0].lower() == 'u':
		return Under(aList)
	elif aList[0].lower() == 'g':
		return Grad(aList)
	elif aList[0].lower() == 'p':
		return Prof(aList)
	elif aList[0].lower() == 'e':
		return Etc(aList)
	else:
		raise NonExistingGroupIdentifier

class Scanner:
	def __init__(self, aFile):
		self.list = aFile.readlines()
		self.objList  = []

	def tokenize(self, aLine):
		return aLine.strip().split()

	def main(self):
		for i in self.list:
			if len(i)<10:
				continue
			try:
				obj = UserFactory(self.tokenize(i))
				obj.formatting()
				self.objList.append( obj )
			except NonExistingGroupIdentifier, IncompleteInputError:
				print 'There is some error. check please.'
				print 'That line is (%s)' % i
			
	def printAllObj(self):
		for i in self.getObjList():
			print str(i)
	
	def getObjList(self):
		return self.objList
	

		
