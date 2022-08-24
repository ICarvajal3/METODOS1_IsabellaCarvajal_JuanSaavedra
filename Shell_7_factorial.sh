read -p "Hasta que número " n

function factorial( ){

fac=1
j=1
for i in $(seq 1 $n)

do
    if [[ $i -eq 1 ]]; then
            echo $i $fac
	    let i=$i+1
    else
            while [[ $j -lt $i ]]
            do
                    let fac=$fac*$i
                    let j=$j+1

            done
	    echo $i $fac
            let i=$i+1
 
    fi
done
}

factorial

