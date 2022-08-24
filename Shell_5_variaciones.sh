#!/bin/bash

f1=1
f2=1

read -p "Escriba un número " n
read -p "Escriba un número " r

p=$((n - r))

function factorial( ){

typeset -i factorial=1

if [ $n -eq 0 ] || [ $n -eq 1 ]; then
        echo $1 $factorial
else
        while [ $n -gt 1 ]
        do
                let factorial=$factorial*$n
                let n=$n-1
		
        done
        f1=$factorial
fi

}




function factorial2( ){

typeset -i factorial2=1

if [ $p -eq 0 ] || [ $p -eq 1 ]; then
        echo $factorial2
else
        while [ $p -gt 1 ]
        do
                let factorial2=$factorial2*$p
                let p=$p-1

        done
	f2=$factorial2
fi

}

factorial
factorial2

#echo $f1 $f2

v=$(( f1 / f2 ))

echo $v
