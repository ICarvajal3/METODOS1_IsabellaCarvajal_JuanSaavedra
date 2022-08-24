#!/bin/bash
array=()

while read line; do
array+=($line)
n=$((n+1))

if [ $n -eq 3 ];then
echo $line
fi

done < lista.dat




