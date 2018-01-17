#!/bin/bash
greet(){
	for name in "$@"
	do 
		echo "Hello $name"
	done
}

greet world class hola

