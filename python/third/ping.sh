#!/bin/bash
if [ "$#" -ne 1 ]
then
	echo "you need one para, such as 122.122.122.122"
    exit
fi

prefix=$(echo $1 | cut -d "." -f 1-3)

for addr in $(seq 0 254)
do 
	ping -c 1 $prefix.$addr | grep "bytes from " | cut -d " " -f 4 | cut -d ":" -f 1
done

