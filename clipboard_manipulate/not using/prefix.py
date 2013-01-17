#prefix.py
import clipboard_lib

def prefix(aString):
    result=[]
    for each in aString.splitlines():
        result.append("> "+each)
    return '\n'.join(result)

if __name__=='__main__':
    clipboard_lib.changeClipboardBy(prefix)
