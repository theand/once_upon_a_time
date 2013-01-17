import unittest
from extract import *

class TestExtract(unittest.TestCase):
    def testAnchor(self):
        s = ( '<a href="atti/Tamo.pdf">', '<a  href = "atti/Tamo.pdf" >')
        self.checkRe(pdfAnchor, s)
        
    def testwholeTag(self):
        s = ( '<a href="atti/as.pdf">wholeTag</a>', '< a href = "atti/as.pdf" ns=s > wholeTag </a>')
        self.checkRe(wholeTag, s)

    def testSubstituteAnchorTag(self):
        s =  '<a href="atti/Tamo.pdf">' #, '<a  href = "atti/Tamo.pdf" >')
        matchedStr = re.search(pdfAnchor, s).group()
        result = re.sub( anchorOpenTag, '', matchedStr)
        result = re.sub( '">', '', result)
        self.assertEquals('atti/Tamo.pdf', result)
        
    def testTitleName(self):
        s =  '<a href="atti/as.pdf">TitleName</a>'
        
        matchedStr = re.search(wholeTag, s).group()
        self.assertEquals( '<a href="atti/as.pdf">TitleName</a>', matchedStr)
        
        result = re.sub( anchorCloseTag, '', matchedStr)
        self.assertEquals('<a href="atti/as.pdf">TitleName', result)

        self.assertEquals( '<a href="atti/as.pdf">', re.search( pdfAnchor, result).group())
        
        result = re.sub( pdfAnchor, '', result)
        self.assertEquals( 'TitleName', result)
        
    def testGetName(self):
        s = ('<a href="atti/as.pdf">TitleName</a>' , '< a href = "atti/as.pdf"> wholeTag </a>')
        expected = ('TitleName', ' wholeTag ')
        result = getName(s[0])
        self.assertEquals( expected[0], result)
        result = getName(s[1])
        self.assertEquals( expected[1], result)

    def testNewLine(self):
        s = ''''< a href = "atti/as.pdf" ns=s > whole
Tag </a>'''
        self.assertEquals(' whole Tag ', getName(s))

    def testComplicated(self):
        s= '''<a href="atti/TammoFreese--EasyMock.pdf">EasyMock:
Dynamic Mock Object for JUnit</a>'''
        self.assertEquals( '''EasyMock: Dynamic Mock Object for JUnit''', getName(s))
            
    def checkRe(self,aPattern,aList): 
        for each in aList: 
            self.assertEquals(each,re.search(aPattern,each).group()) 
    
if __name__ == "__main__":
    unittest.main(argv=('', '-v'))