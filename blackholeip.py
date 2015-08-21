import subprocess
import os
import sys
import getpass
from netaddr import IPNetwork, IPAddress 

# Get user to input IP address to blackhole and verify we own it
unverified_ipaddy = str(raw_input("Enter IP address to blackhole: "))

if IPAddress(unverified_ipaddy) in IPNetwork("207.178.191.0/24"):
	ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("207.178.128.0/17"):
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("209.239.224.0/19"):	# (VCNet block)
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("63.204.233.0/24"):	# (AT&T)
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("209.77.185.0/24"):	# (AT&T)
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("64.160.254.0/24"):	# (AT&T)	
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("64.162.116.0/24"):	# (AT&T)	
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("207.213.112.0/22"):	# (AT&T)	
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("66.127.154.0/24"):	# (AT&T)	
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("207.213.142.0/23"):	# (AT&T)	
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("146.82.174.0/23"):	# (GlobalCrossing block)
        ipaddy = unverified_ipaddy
elif IPAddress(unverified_ipaddy) in IPNetwork("208.84.25.0/24"):	# Customer IP Space, Pleasant Holidays
        ipaddy = unverified_ipaddy
else:
	print('Sorry but you didnt choose an known IP within our owned address space...try again.')
	sys.exit(0) 

# Get user password, username and define global vars
password = raw_input("Enter your router password: ")
username = getpass.getuser()
seq_num = str()

# Open our device list file (read-only), assign a file handle and loop thru the devices
fh = open("device-list.txt","r")
devices = fh.readlines()
for device in devices:
        device = device.rstrip()						# strip out whitespace and carriage returns
	os.system("./getseqnums.sh %s %s %s" % (device,username,password))	# Get sequence num, output to out.txt file
	fname = 'outfiles/out.txt' 						# create handle for out.txt file
	lst = list()								# instantiate our list
	try:
        	fh = open(fname)						# open out.txt file for reading sequence number
	except:
        	print 'File cannot be opened:', fname				# bail if we cannot open out.txt
        	exit()
	for line in fh:								# pull the sequence number from the out.txt file
        	words = line.split()
		if not line.startswith("ip prefix-list Blackhole seq") : continue
		seq_num = words[4] 						# grab the sequence num
		seq_num = int(seq_num)						# convert from string to integer
		seq_num += 1							# increment seq_num 
		seq_num = str(seq_num)						# convert back to string

	os.system("./configure-cisco.sh %s %s %s %s" % (device,password,seq_num,ipaddy)) # configure the router!
