
from cStringIO import StringIO
import clipboard_lib
import re

def remove_space(aString):
    result=[]
    pat = re.compile("\s")
    for each in aString.splitlines():
        each = pat.sub('',each)
        if each != "":
            result.append( each )
    return '\n'.join(result)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(remove_space)
