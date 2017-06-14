#!/usr/bin/python
import os,sys,commands,time,socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))
cdata=s.recvfrom(100)
cdata1=s.recvfrom(100)
if cdata[0] == 'test' and cdata1[0] == '123':
	s.sendto("ok",cdata[1])


