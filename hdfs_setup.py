#!/usr/bin/python
option =''' 
press 1 for setup haddop cluster
press 2 for automatic setup hadoop cluster
'''
print option 
ch = raw_input()
if ch =='1' :
	print "finding ip of all system"
	execfile('ip_cpu.py')
else :
	print "bad choice "
	execfile('menu.py')
