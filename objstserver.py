#!/usr/lib64/python
import os,sys,commands,time,socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))
data=s.recvfrom(20)
d_name=data[0]
while True:
	#data1 will receive drive size
	data1=s.recvfrom(10)
	d_size=data1[0]
	cliaddr=data1[1][0]

	#creating LVM by the name of the client device
	os.system('lvcreate -V'+d_size+'G --name '+d_name+' --thin novavg/pool1')

	#now time for formatting client drive with ext4/xfs
	os.system('mkfs.ext4 /dev/novavg/'+d_name)

	#Creating directory by name of client's drive
	os.system('mkdir /mnt/'+d_name)

	#mounting drive locally
	os.system('mount /dev/novavg/'+d_name+' /mnt/'+d_name)

	#NFS server config
	#os.system('yum install nfs-utils -y')

	#making entry in NFS export file
	entry="/mnt/"+d_name+" "+cliaddr+"(rw,no_root_squash)"

	#Appending this variable to /etc/exports file
	f=open('/etc/exports','a')
	f.write(entry)
	f.write("\n")
	f.close()

	#finally starting nfd service and service persistance
	check=os.system('exportfs -r')
	if check == 0:
		s.sendto("done",data1[1])
	else:
		print "plz check your code"













