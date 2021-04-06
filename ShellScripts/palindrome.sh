#!/bin/sh

echo "Enter the string to be checked: "
read s
len=${#s}
i=$((len - 1))

while [ $i -ge 0 ]
do
	revS=$revS${s:$i:1}
	i=$((i-1))
done

if [ $revS == $s ]
then
	echo "Given string is a palindrome"
else
	echo "Given string is not a palindrome"
fi
