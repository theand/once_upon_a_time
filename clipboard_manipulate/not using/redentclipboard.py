#redentclipboard.py
from cStringIO import StringIO
import clipboard_lib
import redent

INDENT=' '*4
def reindent(aString):
    inFile=StringIO(aString)
    outFile=StringIO()
    redent.go_(inFile,outFile,INDENT)
    return outFile.getvalue()

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(reindent)
