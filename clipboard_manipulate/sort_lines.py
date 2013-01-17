
from cStringIO import StringIO
import clipboard_lib

def sort_lines(aString):
    result=[]
    for each in aString.splitlines():
        each = each.rstrip()
        if each :
            result.append( each )
    result.sort()
    return '\n'.join(result)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(sort_lines)
