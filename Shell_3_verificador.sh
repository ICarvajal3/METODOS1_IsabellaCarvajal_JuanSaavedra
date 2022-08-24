
pass=0

function checkvalue ( ){
        
        read -p "Escriba un número " n

	if [ $n -eq 0 ] || [ $n -eq 1 ]; then
		pass=1
		exit 1
				
	else 
		echo "...intente de nuevo..."	

	fi
}

while [ $pass -eq 0 ]
do 
	 checkvalue
done

checkvalue

