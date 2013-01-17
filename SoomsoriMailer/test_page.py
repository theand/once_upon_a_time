import unittest
import page

class TestPage(unittest.TestCase):
    def setUp(self):
        self.p = page.Page()
        
    def testChkComment(self):
        result = self.p.isComment('# GP9x')
        self.assertEqual(1, result)
        result = self.p.isComment(' theand@sogang.ac.kr')
        self.assertEqual(1, result)
        
    def testNewLine(self):
        result = self.p.isComment('\n')
        self.assertEqual(1, result)
        
    def testEmpty(self):
        result = self.p.isComment('')
        self.assertEqual(1, result)
        
    def testWhiteSpace(self):
        result = self.p.isComment(' ')
        self.assertEqual(1, result)

    def testConversion(self):
        result = self.p.convert('leliena#@korea.com\n')
        self.assertEqual( 'leliena@korea.com', result)
        
    def testAddList(self):
        self.p.AddList('leliena@korea.com')
        self.p.AddList('theand@korea.com')
        self.assertEqual( ['leliena@korea.com','theand@korea.com'], self.p.EmailList)
        
    def testMakeList(self):
        self.p.MakeList('test.txt')
        self.assertEqual( ['leliena@korea.com','theand@korea.com'], self.p.EmailList)
        
    def testSomething(self):
        self.p.MakeList('test.txt')
        print ';'.join(self.p.EmailList)
        

if __name__ == "__main__":
    unittest.main(argv=('','-v'))
