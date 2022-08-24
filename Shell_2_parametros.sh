function help(){

	echo "---Debe incluir tres parametros---"
}

if ! [ $# -eq 3 ]; then
	
	help
	exit 1
else 
	echo "corriendo programa"
fi
