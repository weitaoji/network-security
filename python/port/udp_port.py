#!/usr/bin/python3
import logging
import subprocess
import time
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 4:
	print("you need only one para suck as 122.122.122.1")
addr = sys.argv[1]
begin = int(sys.argv[2])
end = int(sys.argv[3])
for port in range(begin, end):
    print(addr + " " + str(begin) + " " + str(end) + " " + str(port))
    answer = sr1(IP(dst=addr)/UDP(dport=port), timeout=1, verbose=0)
    time.sleep(1)
    print(answer)
    if answer == None:
        print(port)
    else:
        pass

