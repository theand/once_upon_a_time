#!/usr/local/bin/python

import os
import time
import string

dirPrefix = './upload/'
outputfilename = "/home/soomsori/wikidata/theand/text/UploadedFiles"

#------------------------------------------------------------
#여기는 파일 리스트를 만드는 것과 관련된 코드.
def getFileStat(aFileName):
	fp = open(dirPrefix+aFileName)
	fstat = os.fstat( fp.fileno() )
	size ,ctime = fstat[6], fstat[9]
	fp.close()
	ltime = time.localtime(ctime)
	year, month, day = ltime[0],ltime[1],ltime[2]
	return aFileName, size, year, month, day

def makeTable(aFileName, aSize, anYear, aMonth, aDay ):
	
	format = '\n|| [[HTML(<a href="../upload/%s">%s</a>)]] || %s || %04d-%02d-%02d ||'  % ( aFileName, aFileName,aSize, anYear, aMonth, aDay)
	return format

def Title():
	return '\n|| File Name || Size (Byte) || Date ||'

def makeList():
	filelist = os.listdir(dirPrefix)
	list=[]
	list.append(Title())
	for name in filelist:
		f,s,y,m,d = getFileStat(name)
		list.append(makeTable(f,s,y,m,d))
	list.sort()
	str = string.join(list,'')
	return str

def writeFileList(list):
	file = open(outputfilename,"w")
	file.write(list)
	file.close()

def main():
	 writeFileList(makeList())

if __name__ == "__main__":
	main()
