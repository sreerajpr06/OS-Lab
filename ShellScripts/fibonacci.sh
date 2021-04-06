#!/bin/sh

x=0
y=1
echo "Enter the number of terms required in the series: "
read n

if [ $n -lt 1 ]
then
	echo "Invalid value entered!"
elif [ $n -eq 1 ]
then
	echo "${x}"
elif [ $n -eq 2 ]
then
	echo "${x}"
	echo "${y}"
else
	echo $x
	echo $y
	i=2
	while [ $i -lt $n ]
	do
		y=`expr $x + $y`
		x=`expr $y - $x`
		echo $y
		i=`expr $i + 1`
	done
fi	
