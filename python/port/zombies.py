#!/usr/bin/python3
import logging
import subprocess
import time
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def ipid(zombie, port):
    reply1 = sr1(IP(dst=zombie)/TCP(flags="SA", dport=int(port)), timeout=2, verbose=0)
    send(IP(dst=zombie)/TCP(flags="SA", dport=port))
    reply2 = sr1(IP(dst=zombie)/TCP(flags="SA", dport=int(port)), timeout=2, verbose=0)
    try:
        if reply1[TCP].id == (reply2[TCP].id + 2):
            print("it is a good zombie")
            choice = raw_input("do you want to use the zombie? Y/N")
            if choice == "Y":
                target = raw_input("input the target ip addr")
                zombiescan(zombie, target)
            else if choice == "N":
                print("exit...")
    except:
        print("no reply")
        pass
def zombiescan(zombie, target):
    for port int range(1,1000):
        try:
            reply1 = sr1(IP(dst=zombie)/TCP(flags="SA", dport=port), timeout=1, verbose=0)
            send(IP(src=zombie, dst=target)/TCP(flags="S",dport=port), verbose=0)
            reply2 = sr1(IP(dst=zombie)/TCP(flags="SA", dport=port), timeout=1, verbose=0)
                if reply1[TCP].id == (reply2[TCP].id + 2):
                    print(port)
        except:
            pass

if __name__ == "__main__":
    choice = raw_input("1 to test a zombie, 2 use the zombie to send ports to the target")
    if choice == 1:
        zombie = raw_input("input the addr of the zombie")
        ipid(zombie)
    else if choice ==2:
        zombie = raw_input("input the addr of the zombie")
        target = raw_input("input the addr of the target")
        zombiescan(zombie, target)
