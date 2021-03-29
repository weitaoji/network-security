#!/usr/bin/python3
from scapy.all import *
import sys
import _thread

if __name__ == "__main__":
    send(IP(dst='192.168.43.114')/UDP(dport=161)/SNMP(community='cracer', PDU=SNMPbulk(max_repetitions=200, varbindlist=[SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1')), SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.19.1.3'))])))
