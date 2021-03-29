#!/usr/bin/python3
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2: 
	print("you need only one para suck as 122.122.122.1")
	sys.exit()
address = str(sys.argv[1])
prefix = address.split(".")[0] + "." + address.split(".")[1] + "." + address.split(".")[2] + "."
for addr in range(0,254):
    print(prefix+str(addr));
    answer = sr1(IP(dst=prefix+str(addr))/UDP(dport=73456), timeout=1, verbose=0)
    try:
        if int(answer[IP].proto) == 1:
            print(prefix+str(addr))
            #don't used
    except:
        pass
