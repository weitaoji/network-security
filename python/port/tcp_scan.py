#!/usr/bin/python3
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import * 

print('--SEND--')
send = IP(dst="192.168.0.122")/TCP(dport=10000, flags="S")
send.show()
print('\n\n--RECEIVED--')
response = sr1(send, timeout=1, verbose=0)
response.show()
if int(response[TCP].flags) == 18:
    print('\n\n--SEND--')
    reply = sr1(IP(dst="192.168.0.122")/TCP(dport=10000, flags="A", ack=(response[TCP].seq+1)), timeout=1, verbose=0)
    print('\n\n--RECEIVED--')
    reply.show()
