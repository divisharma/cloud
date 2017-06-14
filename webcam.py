#!/usr/bin/python
import os,sys,commands,time,socket,getpass
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip="192.168.122.62"
sport=8888
os.system('ssh -X test@'+sip+' cheese')
execfile('saas.py')
