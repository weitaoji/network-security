#!/bin/bash
if [ "$#" -ne 1 ] 
then
    echo "you need only one para such as 192.168.0.1"
fi

prefix=$(echo $1 | cut -d "." -f 1-3)
for addr in $(seq 0 254):
do
    hping3 $prefix.$addr -c 1 >> r.txt;
done

grep ^len r.txt | cut -d " " -f 2 | cut -d "=" -f 2 >> output.txt
rm -rf r.txt

