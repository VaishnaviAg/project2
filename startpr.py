#!/usr/bin/python
import os,commands,time,getpass
print "welcome to world of data "
time.sleep(2)
user = raw_input("enter user name to access project  ")
password = getpass.getpass()
if user == 'root' and password == 'redhat':
	print "access granted"
	execfile('menu.py')
else :
	print "not granted"
	exit()

