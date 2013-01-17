
from cStringIO import StringIO
import clipboard_lib

def wiki_list(aString):
    result=[]
    for each in aString.splitlines():
        if each.find(" * ") != -1:
            result.append(each.rstrip())
        else:
            each = each.strip()
            if each != "" :
                result.append( " * " + each)
    return '\n'.join(result)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(wiki_list)
