#!/bin/bash
if [ "$#" -ne 1 ]  #num of para != 1
then
    echo "you need one para, such as eth0"
    exit
fi

interface=$1  #the first para
prefix=$(ifconfig $interface | grep 'inet ' | awk '{print $2}' | cut -d "." -f 1-3)  #prefix=192.168.0.119
for addr in $(seq 1 254) 
do 
    arping -c 1 $prefix.$addr | grep 'bytes from' | cut -d " " -f 5 | cut -d "(" -f 2 | cut -d ")" -f 1 >> arp.txt 
done
