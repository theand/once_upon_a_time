#!/usr/local/bin/python2.0

MAILER = 'mailer.cgi'

class UI:
    def __init__(self):
        pass

    def display(self):
        str ="""
<html>
<head>
<title>Soomsori Mailer</title>
<body>
<form method='post' action='%s' >
�����»���ּ�:<input type='text' name="sender_id" maxlength=30><br>
��&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;��:<input type='text' name="subject" ><br>
<textarea name='body' cols='65' rows='15' ></textarea><br>
Password:<input type=password name=PASSWORD size=10 > <input type=submit  value='�߼�'>
</form>
</body>
</html> """ % MAILER
        print str

def send_header():
	print 'Content/type: text/html\n'
	print 


if __name__ == "__main__":
	send_header()
	u = UI()
	u.display()



