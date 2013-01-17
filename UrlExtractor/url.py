import urllib
import urlparse
import os

class Url:
    def __init__(self, aUrl):
        self.url = aUrl
    
    def getBaseUrl(self):
        return 'http://' + urlparse.urlparse(self.url)[1]

    def getJoinedUrl(self, aPath):
        return urlparse.urljoin(self.url, aPath)

    def getDestUrl(self, aTargetUrl):
        if aTargetUrl[0:7] == 'http://':
            dest = aTargetUrl
        else:
            dest = self.getJoinedUrl(aTargetUrl)
        return dest
        
    def storeFileFrom( self, aTargetUrl):
        dest = self.getDestUrl(aTargetUrl)
        targetFile = urllib.urlopen( dest )
                
        urlPath = urlparse.urlparse(dest)[2].split('/')[-1] # get path
        filename = os.path.basename(urlPath)
        outFile = open(filename, 'wb')
        
        while 1:
            s = targetFile.read(8192)
            if not s:
                break
            outFile.write(s)
        targetFile.close()
        outFile.close()
        print 'targetFile(%s) store ok' % filename
        