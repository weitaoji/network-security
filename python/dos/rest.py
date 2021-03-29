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

def shutdown(signalnum, frame):
    print('signalnum:' + str(signalnum) + 'frame:' + str(frame))
if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)
    while True:
        pass


