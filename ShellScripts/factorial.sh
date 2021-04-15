#!/bin/sh

echo "Enter a number: "
read n

fact=1

if [ $n = 0 ]
then
	fact=1
elif [ $n = 1 ]
then
	fact=1
else
	i=2
	temp=`expr $n + 1`
	while [ "$i" != "$temp" ]
	do
		fact=`expr "$fact * $i" | bc` 
		i=`expr $i + 1`
	done
fi

echo "The factorial of ${n} is " $fact
