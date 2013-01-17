import unittest
import re
from url import *

class TestExtract(unittest.TestCase):
    def testGetBaseURl(self):
        u = Url('http://xp2002.org/index.html')
        result = u.getBaseUrl()
        self.assertEqual('http://xp2002.org', result)
        
    def testJoinUrl(self):
        u = Url('http://xp2002.org/index.html')
        result = u.getJoinedUrl('/add/pdf.pdf')
        self.assertEqual('http://xp2002.org/add/pdf.pdf', result)

        u = Url('http://xp2002.org/index.html')        
        result = u.getJoinedUrl( '/add/pdf.pdf')
        self.assertEqual('http://xp2002.org/add/pdf.pdf', result)

        u = Url('http://xp2002.org/index.html')        
        result = u.getJoinedUrl( 'add/pdf.pdf')
        self.assertEqual('http://xp2002.org/add/pdf.pdf', result)

        u = Url( 'http://xp2002.org/temp/index.html')
        result = u.getJoinedUrl( 'add/pdf.pdf')
        self.assertEqual('http://xp2002.org/temp/add/pdf.pdf', result)


if __name__ == "__main__":
    #u = Url('http://www.xp2001.org/xp2001/conference/program.html')
    #u.storeFileFrom('http://www.xp2001.org/xp2001/conference/program.html')
    #u.storeFileFrom('papers/Chapter31-Yongqing+alii.pdf')
    unittest.main(argv=('', '-v'))
