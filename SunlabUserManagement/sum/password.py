


import crypt
import whrandom



def getPasswd(aStr):
	return crypt.crypt(aStr,getSalt())
	

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



