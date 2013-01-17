
from cStringIO import StringIO
import clipboard_lib

def wiki_quote(aString):
    return '{{|\n' + aString + '\n|}}\n'

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(wiki_quote)
