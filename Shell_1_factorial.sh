#!/bin/bash


read -p "Escriba un número " n


typeset -i factorial=1

if [ $n -eq 0 ] || [ $n -eq 1 ]; then
	echo $1 $factorial 
else
	while [ $n -gt 1 ]
	do
		let factorial=$factorial*$n
		let n=$n-1
	done
	echo $1 $factorial
fi

