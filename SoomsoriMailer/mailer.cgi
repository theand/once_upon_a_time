#!/usr/local/bin/python2.0


import cgi
import smtplib
import sys
import traceback

import html_ui
import page

PASSWORD = 'password'
HOST = '127.0.0.1'

FOOTER = """<p>
<img src="http://soomsori.net/logo.jpg" width=200 height=90 >"""

class Mailer:
	def __init__(self):
		self.id= None
		self.subject = None
		self.body = None
		self.passwd = None
		self.page = page.Page()
		self.page.MakeList('/home/soomsori/wikidata/ssr/text/SoomsoriEmailList')

	def parse(self):
		try:
			field = cgi.FieldStorage()
			if field.has_key('sender_id'):
				self.id = field['sender_id'].value
			else:
				self.id = None

			if field.has_key('subject'):
				self.subject = field['subject'].value
			else:
				self.subject = None
			if field.has_key('body'):
				self.body = '<pre>'+ field['body'].value+ '</pre>'+ FOOTER
			else:
				self.body = None
			if field.has_key('PASSWORD'):
				self.passwd = field['PASSWORD'].value
			else:
				self.passwd = None
		except:
			html_ui.send_header()
			print 'CGI ERROR'

		return [self.id,self.subject,self.body]


	def send_mail(self):
		if self.id == None or self.subject==None or self.body == None or self.passwd == None:
			raise InvalidField

		if self.passwd <> PASSWORD:
			raise InvalidPassword


		server =smtplib.SMTP(HOST,25)
		for i in self.page.EmailList:
			mail = ( "From: %s"%self.id , "To : %s"% i, "Subject: %s"%self.subject, "Content-Type: text/html; charset=euc-kr", " ", self.body)
			self.whole_mail = '\r\n'.join(mail)
			server.sendmail(self.id, [i], self.whole_mail)
			print 'Sending to %s is success'%i
		server.quit()


class InvalidPassword:
	def __init__(self):
		pass

class InvalidField:
	def __init__(self):
		pass

if __name__ == "__main__":
	sys.stderr = sys.stdout
	try:
		html_ui.send_header()

		m = Mailer()
		m.parse()
		m.send_mail()
		print 'OK'

	except InvalidPassword:
		print 'Wrong Password'
	except InvalidField:
		print 'Maybe Empty field exists'
	except:
		html_ui.send_header()
		print '\n\n<PRE>'
		traceback.print_exc()

