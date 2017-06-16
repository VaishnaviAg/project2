#!/usr/bin/python
import os,sys,commands,time,getpass,subprocess
ip_list=[]
ip_add='192.168.50.'
for i in range(48)[-3:] :
	check=commands.getstatusoutput('ping -c 1 192.168.50.'+str(i))
	if check[0] == 0 :
		ip_list.append(ip_add+str(i))
else :
	pass
print "scanned ip"
time.sleep(2)
print ip_list

# for cpu
cpu_ram_list=[]
cpu_ram_list_main=[]
cpu_check ="lscpu | grep -i 'CPU(s)' | head -1 | cut -d: -f2 "
#for ram
ram_check="cat /proc/meminfo | grep -i MemTotal"
for i in ip_list :
	cpu_core=commands.getoutput('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+i+" " +cpu_check )
	ram_core=commands.getoutput('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+i+" " +ram_check)
	cpu_ram_list.append(i+str(cpu_core)+"     " +str(ram_core))
	
cpu_ram_list_main=tuple(cpu_ram_list)
for i in cpu_ram_list_main :
	print i
