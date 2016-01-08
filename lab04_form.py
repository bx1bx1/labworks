#!/usr/bin/env python
 
import cgi
from myController import Controller

controll = Controller()
form = cgi.FieldStorage()
 
title = form.getvalue('TEXT_1')
name = form.getvalue('TEXT_2')
message = form.getvalue('TEXT_3')
butt = form.getvalue('butt')

prevObj = form.getvalue('prevObj')
nextObj = form.getvalue('nextObj')

if prevObj is not None and nextObj is not None:
	prevObj = int(prevObj)
	nextObj = int(nextObj)
	
curObj = form.getvalue('curObj')
if curObj is None:
	curObj=0
else:
	curObj = int(curObj)

countObj = controll.getCountObj()

print "Content-type: text/html"

print """
<html>
<head>
	<title>Test URL Encoding</title>
	<link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
"""

if not controll.jsonStatus():
	print "json syntax error\n"
	
	
# ---- navigate Objects ---
if butt is not None:
		controll.setTitle(curObj, title)
		controll.setName(curObj, name)
		controll.setMessage(curObj, message)
		
		# prev Object
		if butt == "<<":
			if (prevObj>=0):
				curObj = prevObj
			else:
				curObj = prevObj + 1
		# next Obj
		if butt == ">>":
			if (nextObj<countObj):
				curObj = nextObj
			else:
				curObj = nextObj - 1
				
		controll.saveData()
				

# ------ form View --------	
print """
	<form action="/cgi-bin/form.py" method="POST">
		<input type="hidden" name="prevObj" value="%d">
		<input type="hidden" name="nextObj" value="%d">
		<input type="hidden" name="curObj" value="%d">
		<table width="500" class="tableClass" border="1" align="center">
			<tr><th>Object %d / %d</th><td></td></tr>
			<tr>
				<td>Title:</td><td> <input type="text" class="smallInpt" name="TEXT_1" value="%s"></td>
			</tr>
			<tr>
				<td>Name:</td><td> <input type="text" class="smallInpt" name="TEXT_2" value="%s"></td>
			</tr>
			<tr>
				<td>Message:</td><td><textarea name="TEXT_3" class="bigInpt">%s</textarea></td>
			</tr>
			<tr>
				<td></td>
				<td align="right">
					<input type="submit" name="butt" value="<<">
					<input type="submit" name="butt" value=">>">
				</td>
			</tr>
		</table>
	</form>
""" % (curObj-1, curObj+1, curObj, curObj+1, countObj, controll.getTitle(curObj), controll.getName(curObj), controll.getMessage(curObj))

print "</body></html>"
