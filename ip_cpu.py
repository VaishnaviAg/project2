#!/usr/bin/python
import os,sys,commands,time,getpass
ip_list=[]
ip_add='192.168.10.'
for i in range(121)[-21:] :
	check=commands.getstatusoutput('ping -c 1 192.168.10.'+str(i))
	if check[0] == 0 :
		ip_list.append(ip_add+str(i))
else :
	pass
print "scanned ip"
time.sleep(2)
print ip_list

# for cpu
cpu_list=[]
cpu_check ="lscpu | grep -i 'CPU(s)' | head -1 | cut -d: -f2"

for i in ip_list :
	cpu_core=commands.getoutput('ssh root@'+i+" " +cpu_check)
	cpu_list.append(i+str(cpu_core))
#for ram 
ram_list=[]
ram_check= 'cat /proc/meminfo | grep -i MemTotal'
for i in ip_list:
	ram_core=commands.getoutput('ssh root@'+i+" "+ram_check)

for i in cpu_list:
	ram_list.append(i + "   " + ram_core)
print ram_list

#for exit
Exit = commands.getoutput('exit')
print Exit
	
