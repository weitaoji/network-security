#!/bin/bash
if [ "$#" -ne 1 ] 
then
    echo "you need a txt or somethong else"
fi
file=$1
for addr in $(cat $file)
do
    arping -c 1 $addr | grep 'bytes from' | cut -d " " -f 5 | cut -d "(" -f 2 | cut -d ")" -f 1 
done
