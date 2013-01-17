

from cStringIO import StringIO
import clipboard_lib

def sort_youtube(aString):
    result=[]
    for each in aString.splitlines():
        each = each.rstrip()
        if each and each.find('http://') >0:
            each = each[each.find('http://'):] + ' ' + each[:each.find('http://'):]
        if each :
            result.append( each )
    result.sort()

    return '\n'.join(result)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(sort_youtube)
