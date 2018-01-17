#!/bin/bash

#This is a comment

echo "Hello world"

myName="Mau"
echo $myName

declare -r NUM1=5
num2=4

num3=$((NUM1+num2))
num4=$((NUM1*num2))
num5=$((NUM1-num2))
num6=$((NUM1/num2))

echo "5 + 4 =  $num3"
echo "5 * 4 =  $num4"
echo "5 - 4 =  $num5"
echo "5 / 4 =  $num6"

num7=1.2
num8=3.4
num9=$(python -c "print $num7+$num8")
echo $num9

cat<< END
This is 
a random
text
END
