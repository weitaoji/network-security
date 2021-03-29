#!/usr/bin/python3
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2: 
	print("you need only one para suck as 122.122.122.1")
	sys.exit()
filename = str(sys.argv[1])
file = open(filename, "r")
for addr in file:
	answer = sr1(IP(dst=addr.strip())/ICMP(), timeout=1, verbose=0)
	if answer == None:
		pass
	else:
		print(addr)	
