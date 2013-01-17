#!/usr/bin/python

"""
# user add script v. 05
# created by Chae Heesang. 2001. 9. 5
# updated 2001. 11. 27
# refactoring using TFP

# run this script daily.
# user information is located at "user.dat"
"""
class NotEnoughElementError: pass

class Token:
    def __init__(self, aFileName):
        import string
        file = open(aFileName,"r")
        tmpLines = file.readlines()
        self.lines = []
        self.list = []
        for i in tmpLines:
       		i = string.strip(i)
       		self.lines.append(i)
       	for i in self.lines:
            self.list.append(string.split(i))
            
    def validate(self):
        import string
        del self.lines
        list = []
        for i in self.list:
            if len(i)!=4:
                raise NotEnoughElementError
            list.append(i)
        self.list=list
        return len(self.list)

def Executor(self, aTokenList):
    pass
