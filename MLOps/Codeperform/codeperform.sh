#!/usr/bin/env bash

# -------------------- help --------------------
help()
{ 
    echo "This is the unhelpful help file. Goodbye."; 
}

# -------------------- main --------------------

while getopts ":h" option; do
   case $option in
      h) # display Help
         help
         exit;;
      *) # invalid cases
         echo 'Invalid option. Find options with flag: -h'
         exit;;
   esac
done



echo "$1"
echo "$2"
