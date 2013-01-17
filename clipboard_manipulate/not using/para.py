#para.py

import textwrap
import clipboard_lib

def paragraph(aString):
    #aString=re.sub(r'(?m)^\s*$','',aString)
    #aString=re.sub(r'(?<!\n)\n(?!\n|$)',' ',aString)
    aString='{{|\n' + aString + '|}}'
    return aString

def wrappara(aString,width=70):
    aString=paragraph(aString)
    widthAdjusted=[]
    for eachLine in aString.splitlines():
        widthAdjusted.append(textwrap.fill(eachLine,width=width))
    return '\n'.join(widthAdjusted)

if __name__=='__main__':
    changeClipboardBy(paragraph)
