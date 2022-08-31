#!/bin/bash

# say hi to version 2

if [ $# = 0 ] 
then
	echo Usage: please include at least one person to greet. 1>&2
	exit 1
elif [ $# = 1 ] 
then
	echo "Hello $1!"
else
	echo -n "Hello $1"
	shift
	for name in $*
	do
		echo -n " and $name"
	done
	echo '!'
fi
exit 0
