#!/bin/sh

echo "Enter a number: "
read n

fact=1

if [ $n = 0 ]
then
	echo aha
	fact=1
elif [ $n = 1 ]
then
	echo oho
	fact=1
else
	i=2
	n=`expr $n + 1`
	while [ "$i" != "$n" ]
	do
		fact=`expr "$fact * $i" | bc` 
		i=`expr $i + 1`
	done
fi

echo "The factorial of ${n} is " $fact
