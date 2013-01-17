import re

anchorOpenTag = '< *a *href *= *"'
anchorCloseTag = '</a>'
word = '[^>].*[^>]'
title = '('+word+')' + '\n*' + '('+word+')*' 
pdfUrl = '.*\.pdf'
pdfAnchor = anchorOpenTag + pdfUrl + '".*>'
wholeTag = pdfAnchor+ title + anchorCloseTag

def getName(aStr):
    m = re.search(wholeTag, aStr)
    if m == None:
        return None
    matchedStr = m.group()
    result = re.sub(anchorCloseTag, '', matchedStr)
    result = re.sub(pdfAnchor, '', result)
    #print result
    return result.replace('\n', ' ')

def getMatchedList(aList):
    list = []
    for each in aList:
        result = re.search(wholeTag, each)
        if result:
            list.append(result.group())
    return list

def printNames(aList):
    for each in aList:
        result = getName(each)
        #print result
        if result:
            print '|| %s ||' % result

def getStrList(aTextChunk):
    list = str.split('</a>')
    list2 = []
    for i in list:
        list2.append(i+'</a>')
    return list2

str='''
	<td width= 900 align="center"><font size="-1"><b><a href="papers/Chapter31-Yongqing+alii.pdf">A great challenge: XP in a typical dot-com</a></b>, 

<i><b>Y. Yongqing, W. Wolff</b></i> - IT department, Europeloan Bank<br>

<b><a href="papers/Chapter24-Peeters.pdf">Simple Design and Unit Testing

with Enterprise JavaBeans? The Box metaphor</a></b>,

<b><i>V. Peeters</i></b> - Tryx bvba<br>

<b><a href="papers/Chapter25-Holcombe+alii.pdf">Functional Test Generation for Extreme Programming</a></b>,

<b><i>M. Holcombe, K. Bogdanov, M. Gheorghe</i></b> - Univ. of Sheffield<br>

<b><a href="papers/Chapter10-Andrea.pdf">Managing the Bootstrap Story in an XP Project</a></b>, 

<b><i>J. Andrea</i></b> - ClearStream Consulting Inc.<br>

<b><a href="papers/Chapter11-Davies.pdf">The Power of Stories</a></b>,

<b><i>R. Davies</i></b> - Connextra Ltd.<br>

<b><a href="papers/Chapter18-Benedicenti+alii.pdf">Using Extreme Programming for Knowledge Transfer</a></b>,

<b><i>L. Benedicenti, R. Paranjape</i></b> - University of Regina<br>

<b><a href="papers/Chapter26-Finsterwalder.pdf">Automating Acceptance Tests for GUI Applications in an Extreme Programming Environment</a></b>,

<b><i>M. Finsterwalder</i></b> - University of Hamburg<br>

<b><a href="papers/Chapter17-Talbott+alii.pdf">Selling XP To The People Who Buy</a></b>,

<b><i>N. Talbott, R.W. Miller</i></b> - RoleModel Software, Inc<br>

<b><a href="papers/Chapter32-Butler+alii.pdf">How Distance Between Subject and Interviewer Affects the Application of Qualitative Research to Extreme Programming</a></b>, 

<b><i>S.J. Butler, Sian Hope, Robert Gittins</i></b> - University of Wales, Bangor<br>

<b><a href="papers/Chapter33-Mertens+alii.pdf">An Example of Product Refactoring</a></b>, 

<b><i>J. Mertens, L. Maknavicius</i></b> - Alcatel R & I, Telecom Services Project<br>

<b>E<a href="papers/Chapter34-Rodrigues+alii.pdf">xtreme Programming on PWAP (ficticious), A Wireless Application</a></b>, 

<b><i>P. Rodrigues, E. Karunakaran</i></b> - NatureSoft Creative Software Solutions Pvt ltd<br>

<b><a href="papers/Chapter35-Bossi+alii.pdf"><i>Repo Margining System</i>: Applying XP in the Financial Industry</a></b>, 

<b><i>P. Bossi, F. Cirillo</i></b> - Banca IMI S.p.A., XPLabs S.R.L.<br>

<b><a href="papers/Chapter36-Marchesi+alii.pdf">Modeling XP Maintenance Activities Using Random Graphs</a></b>, 

<b><i>M. Marchesi, G. Succi, N. Serra</i></b> - Univ. of Cagliari and Univ. of Alberta

'''


if __name__ == '__main__':
    list = getStrList(str)
    list = getMatchedList(list)
    list.sort()
    printNames(list)
