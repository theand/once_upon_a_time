import htmllib
import formatter
import re
class Parser(htmllib.HTMLParser): 
        def __init__(self): 
                htmllib.HTMLParser.__init__(self,formatter.NullFormatter()) 
                self.pdfs=[] 
                self.crntPdfAnchor=None 
        def anchor_bgn(self,aHref,aName,aType): 
                if not self.isPdf(aHref): return 
                self.save_bgn() 
                self.crntPdfAnchor=aHref 
        def anchor_end(self): 
                if not self.crntPdfAnchor:      return 
                text=self.save_end().strip() 
                if self.crntPdfAnchor and text: 
                        self.pdfs.append((text,self.crntPdfAnchor)) 
                self.crntPdfAnchor=None 
        def isPdf(self,aUrl): 
                return re.search('\.pdf$',aUrl)

html="""
<!doctype html public "-//w3c//dtd html 4.0 transitional//en">
<html>
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
   <meta name="GENERATOR" content="Mozilla/4.76 [en] (Windows NT 5.0; U) [Netscape]">
   <title>CS 61A Summer 2002</title>
<link href="cs61a@kurtm.net" rev=made>
</head>

<body bgcolor="#E0E0ff">

<table align="center" width="100%" border="0" cellspacing="0" cellpadding="4">
<tr><td bgcolor="#000000">
<table align="center" width="100%" border="0" cellspacing="0" cellpadding="10">
<table BORDER=0 CELLSPACING=0 CELLPADDING=5 WIDTH="100%" >

<tr BGCOLOR="#303080">
<td VALIGN=BOTTOM><b><font color="#FFFFFF"><center><font size=+2>CS 61A</center></font></font></b></td>
<td VALIGN=BOTTOM><font color="#FFFFFF"><font size=+2><center>
The Structure and Interpretation of Computer Programs</font></font></td>
</tr>

<tr BGCOLOR="#BEBEE0">
<td VALIGN=TOP>
<a  href="pics/sicp_large.jpg">
<img SRC="pics/sicp_small.jpg" height=162 width=130></a>
</td>
<td VALIGN=BOTTOM>
<font size=+3><center>CS61A Summer 2002<br>
MTWTh 11-12:30pm, 1 Pimentel<br></center></font><br>
<hr>
<a href="index.cgi?page=main">News and Calendar</a> |
<a href="index.cgi?page=schedule">Schedule</a> |
<a href="index.cgi?page=staff">Staff</a> |
<a href="index.cgi?page=resources">Resources</a> |
<!-- <a href="http://webcast.berkeley.edu/archive.html?prog=59&group=54">Webcast</a> | -->
<a href="news:ucb.class.cs61a">Newsgroup</a> |
<a href="http://www-inst.eecs.berkeley.edu/webnews">WebNews</a> | 
<!-- <a href="weblabcheck">WebLabCheck</a> | -->
<!-- <a href="readercheck">ReaderCheck</a> | -->
<a href="grading.stds">Standards</a> | 
<a href="old.exams">Past Exams</a>  
</td>
</tr>

</table>
</table>
</table>


&nbsp<br>

<!-- Begin Announcements -->
<a NAME="News"></a>
<table align="center" width="100%" border="0" cellspacing="0" cellpadding="2">
<tr><td bgcolor="#000000">
<table align="center" width="100%" border="0" cellspacing="0" cellpadding="10">
<table BORDER=0 CELLSPACING=2 CELLPADDING=5 WIDTH="100%" >
<tr BGCOLOR="#303080">
<td VALIGN=BOTTOM><font color="#FFFFFF"><font size=+2>
Announcements</font></font></td></tr>

<tr><td bgcolor="#BEBEE0">
<!-- News Table -->

<table border=0 cellpadding=10 cellspacing=0>

<tr valign="top">
<td><nobr><b>8-15-2002</b></nobr></td>
<td><b>Correction from Conceptual Review</b><br>
<ul>
<li>Someone tried the (set! x (amb 3 4)), and it didn't work.  It only picked the first value, and returned
no more values when try-again was attempted</li>
</ul></td></tr>


<tr valign="top">
<td><nobr><b>8-14-2002</b></nobr></td>
<td><b>Midterm 1 solutions posted</b><br>
<ul>
<li>See the standards directory.</li>
<li>Greg says, "Sorry they're so late! I didn't realize that people 
really wanted to see them still."</li>
</ul></td></tr>


<tr valign="top">
<td><nobr><b>8-14-2002</b></nobr></td>
<td><b>The make-up final will take place Thursday 6-9pm.</b><br>
<ul>
<li>Be outside 329 Soda Hall a little before 6 tomorrow night --
we'll move to a room from there.</li>
<li>If you need to take the make-up and have not yet emailed Kurt,
please do so immediately.</li>
</ul></td></tr>


<tr valign="top">
<td><nobr><b>8-14-2002</b></nobr></td>
<td><b>Midterm 3 solutions are up</b><br>
<ul>
<li>See the standards directory. 
</ul></td></tr>


<tr valign="top">
<td><nobr><b>8-05-2002</b></nobr></td>
<td><b>Midterm 2 solutions are up</b><br>
<ul>
<li>See the standards directory. 
</ul></td></tr>


<tr valign="top">
<td><nobr><b><a href="index.cgi?page=oldnews">[Old News]</a></b></nobr></td>

</table>

</table>
</table>
<!-- end announcements -->


&nbsp<br>

<!-- Begin Lecture Reading and Quiz Schedule -->
<a NAME="Calendar"></a>
<table align="center" width="100%" border="0" cellspacing="0" cellpadding="2">
<tr><td bgcolor="#000000">
<table align="center" width="100%" border="0" cellspacing="0" cellpadding="10">
<table BORDER=0 CELLSPACING=2 CELLPADDING=5 WIDTH="100%" >
<tr BGCOLOR="#303080">
<td VALIGN=BOTTOM><font color="#FFFFFF"><font size=+2>
Assignment and Lecture Calendar</font></font></td></tr>
<tr><td bgcolor="#BEBEE0">

<b>Notes:</a>
<ul>
<li>The reading for a given lecture should be done <i>before</i> the lecture.</li> 
<li>Both homeworks for a given week are generally due at 10:00AM on
the Monday <i>after</i> they are assigned.</li>
<li>Labs are ungraded so there is no deadline.</li>
<li>All reading refers to SICP unless noted otherwise.</li>
</ul>

<table border="2" cellpadding="0" cellspacing="0" WIDTH="100%" >
<tr bgcolor="#8E8E8E">
<th ALIGN=LEFT width="10%"><b>Week</b></th>
<th><b>Lecture Topic (and Notes)</b></th>
<th><b>Lab</b></th>
<th><b>Homework</b></th>
<th><b>Reading</b></th>
<th><b>Project</b></th>
</tr>

<tr bgcolor="#F0F0F0">
<td rowspan="4"><b>6/24</b></td>
<td>Mon: <a href="lecnotes/lecn1.1.pdf">Functional Programming</a> I</td>
<td rowspan=2><a href="labs/lab1.1.pdf">Lab 1.1</a></td>

<td rowspan=2><a href="hw/hw1.1.pdf">HW 1.1</a></td>
<td>Mon:</td>
<td rowspan=8><a href="proj/21.pdf">1: Twenty-One</a></td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Tue: Functional Programming II</td>
<td>Tue: 1.1</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Wed: <a href="lecnotes/lecn1.2.pdf">Higher Order Procs</a> I 
<font size=-1><a href="mynotes/1.2.1/notes.scm"> (my notes)</a></font>
</td>
<td rowspan=2><a href="labs/lab1.2.pdf">Lab 1.2</a></td>
<td rowspan=2><a href="hw/hw1.2.pdf">HW 1.2</a></td>
<td>Wed: 1.3</td>
</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Thu: Higher Order Procs II</td>
<td>Thu:</td>
</tr>

<tr bgcolor="#D0D0D0">
<td rowspan="4"><b>7/1</b></td>
<td>Mon: <a href="lecnotes/lecn2.1.pdf">Recursion, Efficiency, et al</a> I
<font size=-1><a href="mynotes/2.1.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab2.1.pdf">Lab 2.1</a></td>
<td rowspan=2><a href="hw/hw2.1.pdf">HW 2.1</a></td>
<td>Mon: 1.2 through 1.2.4</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Tue: Recursion, Efficiency, et al. II</td>
<td>Tue:</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Wed: <a href="lecnotes/lecn2.2.pdf">Data Abstraction</a>
<font size=-1><a href="mynotes/2.2.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab2.2.pdf">Lab 2.2</a></td>
<td rowspan=2><a href="hw/hw2.2.pdf">HW 2.2</a></td>
<td>Wed: 2.1 and 2.2.1</td>
</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Thu: <B>Holiday!</b></td>
<td>Thu:</td>
</tr>



<tr bgcolor="#F0F0F0">
<td rowspan="5"><b>7/8</b></td>
<td>Mon: <a href="lecnotes/lecn3.1.pdf">Hierarchical Data I</a>
<font size=-1><a href="mynotes/3.1.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab3.1.pdf">Lab 3.1</a></td>

<td rowspan=2><a href="hw/hw3.1.pdf">HW 3.1</a></td>
<td>Mon: 2.2.2, 2.2.3, 2.3.1, 2.3.3</td>
<td rowspan=9>2: <a href="proj/painter.pdf">Picture Language</a></td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Tue: Hierarchical Data II</td>
<td>Tue:</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Wed: <a href="lecnotes/lecn3.2.pdf">Abstract Data I</a>
<font size=-1><a href="mynotes/3.2.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab3.2.pdf">Lab 3.2</a></td>
<td rowspan=2><a href="hw/hw3.2.pdf">HW 3.2</a></td>
<td>Wed: 2.4 through 2.5.2</td>
</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Thu: Abstract Data II</td>
<td>Thu:</td>
</tr>
<tr><td bgcolor="#F0D0D0" colspan=4>
Fri: <b>Midterm 1</b> 12:00-2:30 in 1 Pimentel (Covers weeks 1 and 2)
</td></tr>


<tr bgcolor="#D0D0D0">
<td rowspan="4"><b>7/15</b></td>
<td>Mon: <a href="lecnotes/lecn4.1.pdf">Object Oriented Programming I </a><font size=-1>
(<a href="reader/oop/05-2-oopref-man.pdf">reference manual</a>)</font>
<font size=-1><a href="mynotes/4.1.2/notes.scm"> (my notes)</a></font>
</td>
<td rowspan=2><a href="labs/lab4.1.pdf">Lab 4.1</a></td>
<td rowspan=2><a href="hw/hw4.1.pdf">HW 4.1</a></td>
<td>Mon: Reader: <a href="reader/oop/05-1-aboveline.pdf">OOP Pt. I</a></td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Tue: Object Oriented Programming II</td>
<td>Tue:</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Wed: <a href="lecnotes/lecn4.2.pdf">Assignment, State, and Environments I</a>
<font size=-1><a href="mynotes/4.2.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab4.2.pdf">Lab 4.2</a></td>
<td rowspan=2><a href="hw/hw4.2.pdf">HW 4.2</a></td>
<td>Wed: 3.1, 3.2, Reader: <a href="reader/oop/06-belowline.pdf">OOP Pt. II</a></td>
</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Thu: Assignment, State, and Environments II
</td>
<td>Thu:</td>
</tr>

<tr bgcolor="#F0F0F0">
<td rowspan="5"><b>7/22</b></td>
<td>Mon: <a href="lecnotes/lecn5.1.pdf">Mutable Data, Queues, and Tables I</a>
<font size=-1><a href="mynotes/5.1.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab5.1.pdf">Lab 5.1</a></td>

<td rowspan=2><a href="hw/hw5.1.pdf">HW 5.1</a></td>
<td>Mon: 3.3.1 through 3.3.3</td>
<td rowspan=9>3: <a href="proj/adv.pdf">Adventure Game</a></td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Tue: Mutable Data, Queues, and Tables II</td>
<td>Tue:</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Wed: <a href="lecnotes/lecn5.2.pdf">Concurrency I</a>
<font size=-1><a href="mynotes/5.2.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab5.2.pdf">Lab 5.2</a></td>
<td rowspan=2><a href="hw/hw5.2.pdf">HW 5.2</a></td>
<td>Wed: 3.4</td>
</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Thu: Concurrency II</td>
<td>Thu:</td>
</tr>
<tr><td bgcolor="#F0D0D0" colspan=4>
Fri: <b>Midterm 2</b> 12:00-2:00 in 1 Pimentel (Covers weeks 3 and 4)
</td></tr>


<tr bgcolor="#D0D0D0">
<td rowspan="4"><b>7/29</b></td>
<td>Mon: <a href="lecnotes/lecn6.1.pdf">Streams I</a>
<font size=-1><a href="mynotes/6.1.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab6.1.pdf">Lab 6.1</a></td>
<td rowspan=2><a href="hw/hw6.1.pdf">HW 6.1</a></td>
<td>Mon: 3.5.1 through 3.5.5, skip 3.5.4</td>

</tr>
<tr bgcolor="#D0D0D0">
<td>Tue: Streams II</td>
<td>Tue:</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Wed: <a href="lecnotes/lecn6.2.pdf">Meta-Circular Evaluator I</a>
<font size=-1><a href="mynotes/6.2.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab6.2.pdf">Lab 6.2</a></td>
<td rowspan=2><a href="hw/hw6.2.pdf">HW 6.2</a></td>
<td>Wed: 4.1.1 through 4.1.6</td>
</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Thu: Meta-Circular Evaluator II</td>
<td>Thu:</td>
</tr>

<tr bgcolor="#F0F0F0">
<td rowspan="5"><b>8/5</b></td>
<td>Mon: <a href="lecnotes/lecn7.1.pdf">Analyzing and Lazy Evaluators I</a>
<font size=-1><a href="mynotes/7.1.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab7.1.pdf">Lab 7.1</td>

<td rowspan=2><a href="hw/hw7.1.pdf">HW 7.1</a></td>
<td>Mon: 4.1.7, 4.2</td>
<td rowspan=10>4: <a href="proj/logo.pdf">Logo</a></td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Tue: Analyzing and Lazy Evaluators II
<font size=-1><a href="mynotes/7.1.2/notes.scm"> (my notes)</a></font></td></td>
<td>Tue:</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Wed: <a href="lecnotes/lecn7.2.pdf">Non-Deterministic Evaluator I</a>
<font size=-1><a href="mynotes/8.1.1/notes.scm"> (my notes)</a></font></td>
<td rowspan=2><a href="labs/lab7.2.pdf">Lab 7.2</a></td>
<td rowspan=2><a href="hw/hw7.2.pdf">HW 7.2</a></td>
<td>Wed: 4.3</td>
</td>
</tr>
<tr bgcolor="#F0F0F0">
<td>Thu: Non-Deterministic Evaluator II</td>
<td>Thu:</td>
</tr>
<tr><td bgcolor="#F0D0D0" colspan=4>
Fri: <b>Midterm 3</b> 12:00-2:00 in 1 Pimentel (Covers weeks 5 and 6)
</td></tr>

<font size=-1><a href="mynotes/1.2.1/notes.scm"> (my notes)</a></font>

<tr bgcolor="#D0D0D0">
<td rowspan="5"><b>8/12</b></td>
<td>Mon: Non-Deterministic Evaluator III
</td>
<td rowspan=2><a href="labs/lab8.1.pdf">Lab 8.1</a></td>
<td rowspan=2><a href="hw/hw8.1.pdf">HW 8.1</a></td>
<td>Mon: 4.4.1 through 4.4.3</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Tue: <a href="lecnotes/lecn8.1.pdf">Logic Programming I</a>
<font size=-1><a href="mynotes/8.2.1/notes.scm"> (my notes)</a></font></td>
<td>Tue:</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Wed: Logic Programming II</td>
<td rowspan=2>No Lab</td>
<td rowspan=2><a href="hw/hw8.2.pdf">HW 8.2</a></td>
<td>Wed:</td>
</td>
</tr>
<tr bgcolor="#D0D0D0">
<td>Thu: <a href="lecnotes/lecn8.2.pdf">Review</a></td>
<td>Thu:</td>
</tr>
<tr><td bgcolor="#F0D0D0" colspan=4>
Fri: <b>Final Exam</b> 12:00-3:00 in 1 Pimentel (Cumulative; Emphasizes weeks 7 and 8)
</td></tr>

</table>


</table>
</table>
</table>



&nbsp<br>
<hr>
<center>
CS61A, 
<a href="http://www-inst.eecs.berkeley.edu/~cs61a/">http://www-inst.eecs.berkeley.edu/~cs61a/</a><br>
<center>
---------<br>
Last Updated: <i>today</i><br>
Webmaster: <a href="mailto:cs61a@cory.eecs.berkeley.edu">cs61a@cory.eecs</a>
</center>

</body>
</html>

&nbsp<br>
"""
 
p=Parser() 
p.feed(html)
j=0
for i in p.pdfs :
    print 'http://www-inst.eecs.berkeley.edu/~cs61a/' + i[1]
    j+=1



