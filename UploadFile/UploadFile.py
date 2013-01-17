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
link = "http://soomsori.pdauser.net/soletheand/wiki/moin.cgi/�ڷ��"      


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

<h2>���� ���ε�</h2>

<P>
���� %s ���� ������ %.2f kb �� �뷮�� �����ϰ� �ֽ��ϴ�. ( �ִ� ��뷮�� %s kb �Դϴ�.)

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
<HR><CENTER><FONT SIZE="-1"><A HREF="%s">���ư���</A></FONT></CENTER>
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
		msg = "���ε� ������ �̹� %.2f kb �� ������ �ֽ��ϴ�. ���ε念���� �ִ� %s kb �� ũ�Ⱑ ���ѵǾ��ֱ� ������ ���ε尡 �Ұ����մϴ�. �˼��մϴ�." % (kb / 1024.0, maxkb)
		print msg
		print '<HR><CENTER><FONT SIZE="-1"><A HREF="%s">���ư���</A></FONT></CENTER>' % link
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
		msg = "<H2>�� %s ���� ���� %.2f kb �� ���������� ���ε� �Ǿ����ϴ�.:</H2>\n\n" % (len(fnList),kbCount / 1024.0)        
		print msg
		print "<HR><P><UL>"
		for x in range(0,len(fnList)):
		    msg = msg + "  * %s (%.2f kb)\n" % (fnList[x],kbList[x] / 1024.0)
		    print "<LI>%s (%.2f kb)" % (fnList[x],kbList[x] / 1024.0)
		print "</UL>"
		print "<P><HR>"
		    
		print "���� ���ε� ������ %.2f kb �� %s ���� ���ϵ��� �ֽ��ϴ�.<BR>" % ((kb + kbCount) / 1024.0,len(fnList)+len(fns))
		
		print '<HR><CENTER><FONT SIZE="-1"><A HREF="%s">���ư���</A></FONT></CENTER>' % link
	    else:
		print "���ε忡 �����Ͽ����ϴ�."
		print '<HR><CENTER><FONT SIZE="-1"><A HREF="%s">���ư���</A></FONT></CENTER>' % link

	    print "</BODY></HTML>"

	else:
	    form(posturl,len(fns),kb,maxkb,button)

if __name__=='__main__':
	print_header()
	UploadedFiles.main()
	main_body()
	UploadedFiles.main()
