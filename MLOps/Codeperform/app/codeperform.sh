#!/usr/bin/env bash

# exit the script if nonzero status
set -e

# -------------------- help --------------------
help()
{ 
    echo "This is the unhelpful help file. Goodbye."; 
}

# ---------------- set input variables ----------------- 

APP1="$1"
APP2="$2"

# ---------------- time test -----------------
timetest()
{
   # format time to seconds only, real time, 3 significant digits
   TIMEFORMAT=%3R
   # run time function on 
   # use $@ as a general variable input
   TIMETOSTDERR=$({ time "$@" > /dev/null ; } 2>&1)
}

# ---------------- difference -----------------

differencetest()
{
   # run difference on two variables
   # use $@ as a general variable input
   THEDIFFERENCE=$(echo "$1-$2" | bc | awk '{printf "%f", $0}')
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

# use "APP1" to test the first input application
timetest "$APP1"

# assign time to _1 for computation
TIMETOSTDERR_1=$TIMETOSTDERR

# print the output of stracetest
echo "$APP1 execution time was $TIMETOSTDERR seconds."

# use "APP2" to test the second input application
timetest "$APP2"

# assign time to _1 for computation
TIMETOSTDERR_2=$TIMETOSTDERR

# print the output of stracetest
echo "$APP2 execution time was $TIMETOSTDERR seconds."

# execute to find the difference between the variables
differencetest "$TIMETOSTDERR_2"  "$TIMETOSTDERR_1"

# print the difference
echo "the difference between the two is $THEDIFFERENCE"