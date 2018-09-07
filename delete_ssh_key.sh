#!/bin/bash

key_dir = "group"
key_rep = "group/keys"
key =$1

if echo "$key_id" | awk r'/^ssh/{e=1};length($0)<30{e=1};/[[:space:]]+/{e=1};/\@/{e=1}END{if(e)exit(0);else exit(1);}'
then
echo "ERROR: wrong key"
exit 1
fi


grep - l "$key" $key_dir / * | while read file
do
echo - ne "delete key $key from file $file\n"
sed - i "/$key/d" $file
done
