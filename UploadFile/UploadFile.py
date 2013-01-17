#!/usr/local/bin/python

import os
import sys
import cgi
import glob
import string
import UploadedFiles

# ----------------some constant settings----------------------

# directory for upload; will be created if doesn't exist
dirUpload = "./upload" 

# maximum kilobytes to store before no more files accepted
maxkb = 100000   

# a page/url to link at the bottom of page after upload 
link = "http://soomsori.pdauser.net/soletheand/wiki/moin.cgi/자료실"      


#------------------------------------------------------------

def print_header():
	sys.stderr = sys.stdout
	print "content-type: text/html"
	print 


def form(posturl,files,kb,maxkb,button):
    "Print the main form."
    print """<html>
<head>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;charset=euc-kr">
<title>File Upload</title>
<body>

<h2>파일 업로드</h2>

<P>
현재 %s 개의 파일이 %.2f kb 의 용량을 차지하고 있습니다. ( 최대 허용량은 %s kb 입니다.)

<form action="%s" method="POST" enctype="multipart/form-data">
Name of File 1: <input name="file.1" type="file" size="35">
<BR>
Name of File 2: <input name="file.2" type="file" size="35">
<BR>
Name of File 3: <input name="file.3" type="file" size="35">
<BR>
<!--
Name of File 4: <input name="file.4" type="file" size="35">
<BR>
Name of File 5: <input name="file.5" type="file" size="35">
-->
<P>
<input name="submit" %s>
</form>
<HR><CENTER><FONT SIZE="-1"><A HREF="%s">돌아가기</A></FONT></CENTER>
</body>
</html>
""" % (files,kb/1024.0,maxkb,posturl,button,link)



def main_body():
	if os.environ.has_key("HTTP_USER_AGENT"):
	    browser = os.environ["HTTP_USER_AGENT"]
	else:
	    browser = "No Known Browser"

	if os.environ.has_key("SCRIPT_NAME"):
	    posturl = os.environ["SCRIPT_NAME"]
	else:
	    posturl = ""

	kb = 0

	fns = glob.glob(dirUpload+os.sep+"*")
	for x in fns:
	    kb = kb + os.stat(x)[6]

	if kb/1024<maxkb:
	    button = 'type="submit" value="Upload File(s)"'
	else:
	    button = 'type="button" value="Upload Disabled (maximum KB reached)"'

	data = cgi.FieldStorage()


	if data.has_key("file.1"):  # we have uploads.

	    if kb/1024>maxkb:
		print "<HTML><HEAD><TITLE>Upload Aborted</TITLE></HEAD><BODY>"
		msg = "업로드 영역에 이미 %.2f kb 의 파일이 있습니다. 업로드영역은 최대 %s kb 로 크기가 제한되어있기 때문에 업로드가 불가능합니다. 죄송합니다." % (kb / 1024.0, maxkb)
		print msg
		print '<HR><CENTER><FONT SIZE="-1"><A HREF="%s">돌아가기</A></FONT></CENTER>' % link
		print "</BODY></HTML>"
		sys.exit()

	    if not os.path.exists(dirUpload):
		os.mkdir(dirUpload,0777)

	    fnList = []
	    kbList = []
	    kbCount = 0
	    f = 1
	    while f:
		key = "file.%s" % f
		if data.has_key(key):
		    fn = data[key].filename
		    if not fn:
			f = f + 1
			continue
		    if string.rfind(data[key].filename,"\\") >= 0:
			fn = fn[string.rfind(data[key].filename,"\\"):]
		    if string.rfind(data[key].filename,"/") >= 0:
			fn = fn[string.rfind(data[key].filename,"/"):]
		    if string.rfind(data[key].filename,":") >= 0:
			fn = fn[string.rfind(data[key].filename,":"):]

		    o = open(dirUpload+os.sep+fn,"wb")
		    o.write(data[key].value)
		    o.close()

		    fnList.append(fn)
		    kbList.append(len(data[key].value))
		    kbCount = kbCount + len(data[key].value)
		    f = f + 1
		else:
		    f = 0


	    print '<HTML><HEAD><META HTTP-EQUIV="Content-Type" CONTENT="text/html;charset=euc-kr"><TITLE>Upload Results</TITLE></HEAD><BODY>'
	    if len(fnList):
		msg = "<H2>총 %s 개의 파일 %.2f kb 가 성공적으로 업로드 되었습니다.:</H2>\n\n" % (len(fnList),kbCount / 1024.0)        
		print msg
		print "<HR><P><UL>"
		for x in range(0,len(fnList)):
		    msg = msg + "  * %s (%.2f kb)\n" % (fnList[x],kbList[x] / 1024.0)
		    print "<LI>%s (%.2f kb)" % (fnList[x],kbList[x] / 1024.0)
		print "</UL>"
		print "<P><HR>"
		    
		print "현재 업로드 영역에 %.2f kb 의 %s 개의 파일들이 있습니다.<BR>" % ((kb + kbCount) / 1024.0,len(fnList)+len(fns))
		
		print '<HR><CENTER><FONT SIZE="-1"><A HREF="%s">돌아가기</A></FONT></CENTER>' % link
	    else:
		print "업로드에 실패하였습니다."
		print '<HR><CENTER><FONT SIZE="-1"><A HREF="%s">돌아가기</A></FONT></CENTER>' % link

	    print "</BODY></HTML>"

	else:
	    form(posturl,len(fns),kb,maxkb,button)

if __name__=='__main__':
	print_header()
	UploadedFiles.main()
	main_body()
	UploadedFiles.main()
