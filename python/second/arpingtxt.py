#!/usr/bin/python3
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2: 
	print("you need only one para such as arp.txt or something")
	sys.exit()
filename = sys.argv[1]
file = open(filename, 'r')
for addr in file:
	answer = sr1( ARP(pdst = str(addr)), timeout=0.1, verbose=0)
	print(answer)
	if answer == None:
		pass
	else:
		print(addr)
	
