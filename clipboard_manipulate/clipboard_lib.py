import win32clipboard as w
import win32con,re,textwrap

def getText():
    w.OpenClipboard()
    d=w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def setText(aString,aType=win32con.CF_TEXT):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(aType,aString)
    w.CloseClipboard()

def changeClipboardBy(aFunc):
    result=aFunc(getText().replace('\r\n','\n'))
    setText(result.replace('\n','\r\n'))
