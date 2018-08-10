#!/bin/bash

key_dir="group"
key_rep="group/keys"
key=$1

test -z "$key" && exit 1

grep -l "$key" $key_dir/* | while read file; do
        echo -ne "delete key $key from file $file\n"
        sed -i "/$key/d" $file
done

