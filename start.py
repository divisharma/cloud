#!/usr/bin/python
import os,sys,commands,time,socket,getpass
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip="192.168.122.62"
sport=8888
print "cloud servers reloaded...enter authentication details:"
suser=raw_input("enter username : ")
spassword=getpass.getpass()
s.sendto(suser,(sip,sport))
s.sendto(spassword,(sip,sport))
sdata=s.recvfrom(2)
if sdata[0]=="ok":
	print "authentication done"
	print "wait for services"
	time.sleep(2)
	execfile('saas.py')
else:
	print "check your user details"
exit()

