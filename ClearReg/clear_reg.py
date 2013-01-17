import _winreg

class ClearReg:
	def __init__(self):
		key_mp = r'SOFTWARE\Microsoft\MediaPlayer\Player\RecentURLList'
		key_ie_typed_url = r'SOFTWARE\Microsoft\Internet Explorer\TypedURLs'

		self.shell_key_mp = _winreg.OpenKey( _winreg.HKEY_CURRENT_USER, key_mp, 0, _winreg.KEY_SET_VALUE )
		self.shell_ie_typed_url = _winreg.OpenKey( _winreg.HKEY_CURRENT_USER, key_ie_typed_url, 0, _winreg.KEY_SET_VALUE )

	def getMpLruValue(self, aNum):
		value, type = _winreg.QueryValueEx( self.shell_key_mp, 'URL%d'%aNum)
		return value.lower()

	def delMpLru(self, aNum):
		_winreg.SetValueEx(self.shell_key_mp, 'URL%d'%aNum, 0, _winreg.REG_SZ, '')
		
	def delAllMpLru(self):
		for i in range(20):
			self.delMpLru(i)
		
	def getRpKey(self, aNum):
		key_rp = r'Software\RealNetworks\RealPlayer\6.0\Preferences\MostRecentClips%d'%aNum
		self.shell_key_rp = _winreg.OpenKey( _winreg.HKEY_CLASSES_ROOT, key_rp, 0, _winreg.KEY_SET_VALUE )
		value, type = _winreg.QueryValueEx( self.shell_key_rp, '')
		return value.lower()
		
	def delRpKey(self, aNum):
		key_rp = r'Software\RealNetworks\RealPlayer\6.0\Preferences\MostRecentClips%d'%aNum
		self.shell_key_rp = _winreg.OpenKey( _winreg.HKEY_CLASSES_ROOT, key_rp, 0, _winreg.KEY_SET_VALUE )
		_winreg.SetValueEx( self.shell_key_rp, '', 0, _winreg.REG_SZ, '')	

	def delAllRpList(self):
		for i in range(1, 9):
			self.delRpKey(i)

	def getTypedUrl(self, aNum):
		value, type = _winreg.QueryValueEx( self.shell_ie_typed_url, 'url%d'%aNum)
		return value.lower()

	def delTypedUrl(self, aNum):
		_winreg.SetValueEx( self.shell_ie_typed_url, 'url%d'%aNum, 0, _winreg.REG_SZ, '')	
		
	def delAllTypedUrl(self):
		for i in range(1, 30):
			self.delTypedUrl(i)

if __name__ == "__main__":
	c = ClearReg()
	c.delAllMpLru()
	c.delAllRpList()
	c.delAllTypedUrl()

