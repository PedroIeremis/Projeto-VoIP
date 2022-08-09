#!/bin/bash

echo > process.txt
cat x.txt | tr -d "}" | tr -d "{" | tr -d '"' | tr ',' '.' > x2.txt

while read x y
do

if [ $x == 'cep:' ];then
	x1=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x1 $y >> process.txt
elif [ $x == 'logradouro:' ];then
	x2=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x2 $y >> process.txt
elif [ $x == 'bairro:' ];then
        x3=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x3 $y >> process.txt
elif [ $x == 'localidade:' ];then
        x4=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x4 $y >> process.txt
elif [ $x == 'uf:' ];then
	x5=$(echo $x | sed 's/:/, corresponde a/g')
        echo $x5 $y >> process.txt
elif [ $x == 'ddd:' ];then
        x6=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x6 $y >> process.txt
fi

done < x2.txt

rm x.txt
rm x2.txt
