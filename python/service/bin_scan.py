#!/usr/bin/python3
import socket
import select
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("you need two para")
        sys.exit()
    
    ip = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    
    for port in range(start, end):
        try:
            banner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            banner.connect((ip, port))
            ready = select.select([banner],[],[],1)
            if not ready[0]:
                print("TCP port" + str(port) + "-" + banner.recv[4096])
                banner.close()
        except:
            pass
