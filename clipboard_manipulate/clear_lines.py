
from cStringIO import StringIO
import clipboard_lib

def wiki_clear_lines(aString):
    result=[]
    for each in aString.splitlines():
        each = each.strip()
        if each != "":
            result.append(each)
    return '\n'.join(result)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(wiki_clear_lines)
