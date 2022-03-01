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
   TIME=$(strace -c "$1" 2>&1 >/dev/null | awk 'END{print $2}');
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

# use "$@" since function's $1 is script's $1
"$@" stracetest
echo "$TIME"

echo "$1"
echo "$2"
