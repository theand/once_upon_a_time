
from cStringIO import StringIO
import clipboard_lib

def blog_quote(aString):
    return '<<' + aString + '>>'

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(blog_quote)
