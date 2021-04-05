#!/bin/sh

echo "Enter the value of 'n': "
read n

i=1
sum=0
while [ "$i" != `expr $n + 1` ]
do
	read num
	sum=`expr $num + $sum`
	i=`expr $i + 1`
done

echo "Sum of ${n} numbers : " $sum

