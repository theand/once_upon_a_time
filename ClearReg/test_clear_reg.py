
import unittest
import clear_reg

class TestClearReg(unittest.TestCase):
	def setUp(self): 
		self.c = clear_reg.ClearReg()

	def testGetKey(self):
		result = self.c.getMpLruValue(1)
		self.assertEqual('', result)
		
	def testDelKey(self):
		self.c.delMpLru(0)
		result = self.c.getMpLruValue(0)
		self.assertEqual( '', result)

	def testDelAllMp(self):
		self.c.delAllMpLru()
		result = self.c.getMpLruValue(1)
		self.assertEqual('', result)

	def testGetRpKey(self):
		result = self.c.getRpKey(1)
		self.assertEqual( '', result)

	def testDelRpKey(self):
		self.c.delRpKey(2)
		result = self.c.getRpKey(2)
		self.assertEqual( '', result)

	def testDelAllRp(self):
		self.c.delAllRpList()
		result = self.c.getRpKey(1)
		self.assertEqual( '', result)

	def testGetTypedUrl(self):
		result = self.c.getTypedUrl(1)
		self.assertEqual( '', result)
		
	def testDelTypedUrl(self):
		self.c.delTypedUrl(2)
		result = self.c.getTypedUrl(2)
		self.assertEqual( '', result)
		
	def testDellAllTypedUrl(self):
		self.c.delAllTypedUrl()
		result = self.c.getTypedUrl(2)
		self.assertEqual( '', result)



if __name__ == '__main__':
	unittest.main(argv=('', '-v'))

