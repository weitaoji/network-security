#!/usr/bin/python3
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys

if len(sys.argv) != 2:
    print("you need one para")
    sys.exit()
ip = sys.argv[1]
answer = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
if answer == None:
    print("no response")
elif int(answer[IP].ttl) <= 64:
    print("Host is Linux/Unix")
else:
    print("Host is Windows")
