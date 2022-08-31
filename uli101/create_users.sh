#!/bin/bash

# Create directories for each student.

attendance="$1"
user_dir="users" # In the real world, we create these in /home!
backup_dir="backup"
today=$(date '+%Y-%m-%d') # Don\'t worry about remembering this! It\'s just an example..
echo "Today is: "$today"."

if [ ! -d "$backup_dir"/"$today" ] 
then
	mkdir "$backup_dir"/"$today"
fi

if [ ! -f "$attendance" ] 
then
	echo ""$attendance" not found."
	exit 1
fi

echo "Reading from "$attendance"..."
while read input
do
	if [ -d "$user_dir"/"$input" ]
	then
		mv "$user_dir"/"$input" "$backup_dir"/"$today"
	fi
	mkdir users/"$input"
	echo "Created "$input"."
done < $attendance
