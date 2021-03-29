#!/usr/bin/python3
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2: 
	print("you need only one para")
	sys.exit()

interface = str(sys.argv[1])
ip = subprocess.check_output("ifconfig " + interface + " | grep 'inet ' | awk '{print $2}' | cut -d '.' -f 1-3", shell=True).strip()
for addr in range(0,254):
	answer = sr1( ARP(pdst = str(ip,encoding="utf-8") + "." + str(addr)), timeout=0.1, verbose=0)
	if answer == None:
		pass
	else:
		print(str(ip,encoding="utf-8") + "." + str(addr))
