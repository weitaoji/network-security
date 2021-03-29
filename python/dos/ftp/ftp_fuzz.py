#!/usr/bin/python3
import socket
import sys

if len(sys.argv) != 5:
    print('./ftp_fuzz [ip] [port]  [step] [max_length]')
    print('./ftp_fuzz 1.1.1.1 21 100 1000')
    sys.exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])
step = int(sys.argv[3])
i = int(sys.argv[3])
max_length = int(sys.argv[4])

user = input(str('ftp account:'))
password = input(str('ftp password:'))
command = input(str('ftp command:'))
 
while i <= max_length:
   try:
       payload = command + " " + '\n'*i
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
       print(str(i) + ':' + '\n')                            
       s.connect((ip, port))                                 
       print(s.recv(1024))                                   
       s.send(b'USER ' + bytes(user, encoding='utf-8') + b'\r\n') 
       print(s.recv(1024))                                   
       s.send(b'PASS ' + bytes(password, encoding='utf-8') + b'\r\n')                   
       print(s.recv(1024))                                   
       s.send(bytes(payload, encoding='utf-8') + b'\r\n')
       s.send(b'QUIT\r\n') 
       s.close()                                             
       i = i + step
   except:
       print('server is died')
       sys.exit()
print('no buffer_exploit')
