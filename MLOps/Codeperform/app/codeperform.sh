#!/usr/bin/env bash

# -------------------- help --------------------
help()
{ 
    echo "This is the unhelpful help file. Goodbye."; 
}

# ---------------- strace test -----------------
stracetest()
{
   # run strace -c on first input and print out the average execution time
   # use $@ as a general variable input
   TIME=$(strace -c "$@" 2>&1 >/dev/null | awk 'END{print $2}');
}

# ---------------- set input variables ----------------- 

APP1="$1"
APP2="$2"


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

# use "APP1" to test the first input application
stracetest "$APP1"

# print the output of stracetest
echo "APP1 execution time was $TIME seconds."

# use "APP2" to test the second input application
stracetest "$APP2"

# print the output of stracetest
echo "APP2 execution time was $TIME seconds."