#!/usr/bin/python3
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 3:
    print("you need two para such as 192.168.0.126 25 to check the firewall")
    sys.exit()

addr = sys.argv[1]
port = int(sys.argv[2])
syn_pack = sr1(IP(dst=addr)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
ack_pack = sr1(IP(dst=addr)/TCP(dport=port, flags="A"), timeout=1, verbose=0)


if (int(syn_pack[TCP].flags) == 18) and (int(ack_pack[TCP].flags) == 4):
    print("port is unfiltered or opened")
elif ((int(syn_pack[TCP].flags) == 18) and (ack_pack == None)) or ((syn_pack == None) and (int(ack_pack[TCP].flags) == 4)):
    print("port is filtered")
else: 
    print("host is down or port is closed")
