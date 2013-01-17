#-*-coding:mbcs-*- #
#calc.py
from cStringIO import StringIO
import clipboard_lib
import sys,traceback
import win32com.client,win32gui,win32api

def captureStdout(aFunc,*args,**kwargs):
    saved=sys.stdout
    sys.stdout=StringIO()
    returnValue=aFunc(*args,**kwargs)
    output=sys.stdout.getvalue()
    sys.stdout=saved #sys.__stdout__
    return output,returnValue

def getDict():
    return {'wrap':para.wrappara}

def _execute(s):
    try:
        exec s in getDict()
    except:
        traceback.print_exc()

def _eval(s):
    try:
        value=eval(s,getDict())
    except SyntaxError:
        raise
    except:
        traceback.print_exc()
    if value:
        hprint(value)  #hprint는 print ['어쩌구','저쩌구'] 등을 했을 때 한글이 제대로 찍히는 pprint입니다.

def capturedFuncFactory(aFunc):
    def _captured(*args):
        result,_=captureStdout(aFunc,*args)
        return result
    return _captured

executeStatement=capturedFuncFactory(_execute)
evalExpression=capturedFuncFactory(_eval)

def calculate(aString):
    if aString.startswith('!'):
        import template
        return template.template[aString[1:]]
    try:
        z=evalExpression(aString)
    except SyntaxError:
        z=executeStatement(aString)
    return z

if __name__=='__main__':
    saved=para.getText()
    s=win32com.client.gencache.EnsureDispatch("WScript.Shell")
    thisApp=win32gui.GetForegroundWindow()
    s.AppActivate(thisApp)
    s.SendKeys("^c")
    win32api.Sleep(100)
    clipboard_lib.changeClipboardBy(calculate)
    win32api.Sleep(100)
    s.SendKeys("^v")
    para.setText(saved)
    win32api.Sleep(100)
