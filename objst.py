#!/usr/bin/python
import os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip="192.168.122.62"
sport=8888
drive_name=raw_input("Enter storage driver name : ")
drive_size=raw_input("Enter size in MB: ")
s.sendto(drive_name,(sip,sport))
s.sendto(drive_size,(sip,sport))
res=s.recvfrom(4)
if res[0] == "done":
	os.system('mkdir /media/'+drive_name)
	os.system('mount '+sip+':/mnt/'+drive_name+' /media/'+drive_name)
else:
	print "No response from storage cloud"

