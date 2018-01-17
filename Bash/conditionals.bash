#!/bin/bash

read -p "What is your name?" name

echo "Hello $name"

read -p "How old are you" age

if [ $age -ge 16 ]
then 
	echo "You are young"
elif [ $age -eq 20 ] 
then
	echo "Shalala"
else
	echo "Jojojo"
fi
