#!/bin/bash

echo > /usr/share/asterisk/agi-bin/process.txt
cat /usr/share/asterisk/agi-bin/x.txt | tr -d "}" | tr -d "{" | tr -d '"' | tr ',' '.' > /usr/share/asterisk/agi-bin/x2.txt

while read x y
do

if [ $x == 'cep:' ];then
	x1=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x1 $y >> /usr/share/asterisk/agi-bin/process.txt
elif [ $x == 'logradouro:' ];then
	x2=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x2 $y >> /usr/share/asterisk/agi-bin/process.txt
elif [ $x == 'bairro:' ];then
        x3=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x3 $y >> /usr/share/asterisk/agi-bin/process.txt
elif [ $x == 'localidade:' ];then
        x4=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x4 $y >> /usr/share/asterisk/agi-bin/process.txt
elif [ $x == 'uf:' ];then
	x5=$(echo $x | sed 's/:/, corresponde a/g')
        echo $x5 $y >> /usr/share/asterisk/agi-bin/process.txt
elif [ $x == 'ddd:' ];then
        x6=$(echo $x | sed 's/:/, corresponde a/g')
	echo $x6 $y >> /usr/share/asterisk/agi-bin/process.txt
fi

done < /usr/share/asterisk/agi-bin/x2.txt

rm /usr/share/asterisk/agi-bin/x.txt
rm /usr/share/asterisk/agi-bin/x2.txt
