import unittest
from ua import *

class TokenTest(unittest.TestCase):
    def testGetLine(self):
        theTokenList = Token("user.dat")
        self.assertEqual( theTokenList.lines[0], "U 991033 password ChaeHeeSang")

    def testGetToken(self):
        token = Token("user.dat")
        self.assertEqual( token.list[0],["U","991033","password","ChaeHeeSang"])

    def testValidation(self):
        token = Token("user.dat")
        self.assertEqual( token.validate(), 1)


class ExecTest(unittest.TestCase):
    def testInit(self):
        t = Token("user.dar")
        e = Executor(t)
        assertEqual(e,"useradd cs991033 -c ChaeHeeSang -g under -d /home/under/cs991033 -p")
        

if __name__ == "__main__":
    unittest.main()
    