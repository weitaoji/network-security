#!/usr/bin/python3
import sys
import socket

if len(sys.argv) != 2:
    print("you need one para")
    sys.exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("smtp.163.com", 25))
banner = s.recv(1024)
print(banner + "aaaaaaa")
s.send("VRFY" + sys.argv[1] + "\r\n")

# need more
# need more
# need more

result = recv(1024)
print(result)
s.close()
