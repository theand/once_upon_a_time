

from cStringIO import StringIO
import clipboard_lib

def sort_youtube(aString):
    result=[]
    for each in aString.splitlines():
        each = each.rstrip()
	if each and each[0] == "-":
	    each = each[1:] + ' -'
        if each :
            result.append( each )
    result.sort()

    final = []
    for each in result:
        if each and each[-1] == '-':
		each = '-' + each[:-1].rstrip()
        final.append(each)
    return '\n'.join(final)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(sort_youtube)
