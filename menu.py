#!/usr/bin/python 
import os ,time,commands,getpass
option ='''
press1 for setup hadoop cluster 
press2 for setup MR
press 3 for setup HIVE'''
print option
ch =raw_input()
if ch == '1' :
	print "processing for setup cluster"
	execfile('hdfs_setup.py')
elif ch == '2' :
	print "make sure you have enough amount to cpu stores"
	execfile('mr_setup.py')
else :
	print "wrong option"
	execfile('startpr.py')

