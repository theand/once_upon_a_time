
from cStringIO import StringIO
import clipboard_lib

def wiki_http_prefix(aString):
    result=[]
    for each in aString.splitlines():
        each = each.strip()
        if each != "":
            result.append( "http://" + each)
    return '\n'.join(result)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(wiki_http_prefix)
