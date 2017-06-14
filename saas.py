#!/usr/bin/python
import os,sys,time
x="""
Press 1 to get firefox
Press 2 to get vlc
Press 3 to get calculator
Press 4 to get office
Press 5 for screenshot
Press 6 for webcam
"""

print x
ch = raw_input("enter your choice")

if ch == '1':
	execfile('firefox.py')
elif ch == '2':
	execfile('vlc.py')
elif ch == '3':
	execfile('calc.py')
elif ch == '4':
	execfile('office.py')
elif ch == '5':
	execfile('ss.py')
elif ch == '6':
	execfile('webcam.py')

else:
	print "wrong choice"

