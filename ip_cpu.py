#!/usr/bin/python
import os,sys,commands,time,getpass,subprocess
ip_list=[]
ip_add='192.168.10.'
for i in range(119)[-19:] :
	check=commands.getstatusoutput('ping -c 1 192.168.10.'+str(i))
	if check[0] == 0 :
		ip_list.append(ip_add+str(i))
else :
	pass
print '\033[1m' "Reachable ip.."
print '\033[0m'
time.sleep(2)
print ip_list

cpu_ram_list=[]
cpu_ram_list_main=[]
#for cpu
cpu_check ="lscpu | grep -i 'CPU(s)' | head -1 | cut -d: -f2 "
#for ram
ram_check="cat /proc/meminfo | grep -i MemTotal"
for i in ip_list :
	cpu_core=commands.getoutput('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+i+" " +cpu_check )
	ram_core=commands.getoutput('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+i+" " +ram_check)
	if "WARNING" not in cpu_core and "WARNING" not in ram_core :
	     cpu_ram_list.append(i+str(cpu_core)+"     " +str(ram_core))
	
cpu_ram_list_main=tuple(cpu_ram_list)
for i in cpu_ram_list_main :
	print i
