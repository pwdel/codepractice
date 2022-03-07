#!/usr/bin/env bash

# exit the script if nonzero status
set -e

# ---------------- help --------------------------------
help()
{ 
    echo " |--------------------------------- codeperform v0.0.1 -------------------------------------------| ";
    echo "               Copyright (c) 2022  - Free Software Under the MIT License  ";
    echo " description:  codeperform uses the builtin bash time function to printout statistics on the";
    echo "               real-time performance  of binary and python applications.";
    echo "               both python and binary files can be used or tested against each other.";    
    echo " usage:        codeperform [file] [file] ";
    echo " formatting:   binary files should be enclosed in single quotes    ---> ./binaryfile  ";
    echo "               python files do not require quotes                  ---> pythonfile.py .";    
    echo " |------------------------------------------------------------------------------------------------| ";    
}

# ---------------- set input variables ----------------- 

APP1="$1"
APP2="$2"

# ---------------- input test --------------------------

apptype()
{
   # if the input program has .py, then it's python
   if echo "$@" | grep -q .py; then
      APPTYPE="python"
   else
      APPTYPE="unknown"
   fi
}


# ---------------- time test ---------------------------
timetest()
{
   # format time to seconds only, real time, 3 significant digits
   TIMEFORMAT=%3R
   if [ "$APPTYPE" == "unknown" ]; then
      # run time function on 
      # use $@ as a general variable input
      TIMETOSTDERR=$({ time "$@" > /dev/null ; } 2>&1)
   elif [ "$APPTYPE" == "python" ]; then
      TIMETOSTDERR=$({ time python3 "$@" > /dev/null ; } 2>&1)
   fi
}

# ---------------- difference ---------------------------

differencetest()
{
   # run difference on two variables
   # use $@ as a general variable input
   THEDIFFERENCE=$(echo "$1-$2" | bc | awk '{printf "%.3f", $0}')
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

# test the apptype for APP1
apptype "$APP1"

# use "APP1" to test the first input application
timetest "$APP1" "$APPTYPE"

# assign time to _1 for computation
TIMETOSTDERR_1=$TIMETOSTDERR

# print the output of stracetest
echo "$APP1 execution time was $TIMETOSTDERR seconds."

# test the apptype for APP2
apptype "$APP2"

# use "APP2" to test the second input application
timetest "$APP2" "$APPTYPE"

# assign time to _1 for computation
TIMETOSTDERR_2=$TIMETOSTDERR

# print the output of stracetest
echo "$APP2 execution time was $TIMETOSTDERR seconds."

# execute to find the difference between the variables
differencetest "$TIMETOSTDERR_2"  "$TIMETOSTDERR_1"

# print the difference
echo "the difference between ($APP1) - ($APP2) is $THEDIFFERENCE seconds."