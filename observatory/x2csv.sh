#!/bin/sh
echo "Please input Sensor ID!"
read SID
echo "Please input Obs No.!"
read OBS

INPUT_FILE="$SID*.xlsx"

if [ -f ${INPUT_FILE} ] ; then
  echo $INPUT_FILE
  case "$SID" in

    TD*)
    xlsx2csv -p "" -I "Data" -a $INPUT_FILE| sed -e "4,$ s/Data//g" -e "4,$ s/Time,Temperature,Pressure,Sea pressure,Depth//g" -e '/^$/d' > "${SID}_${OBS}_obs_full.csv"
    ;;

    T*)
    xlsx2csv -p "" -I "Data" -a $INPUT_FILE | sed -e "4,$ s/Data//g" -e "4,$ s/Time,Temperature//g" -e '/^$/d' > "${SID}_${OBS}_obs_full.csv"
    ;;

    
    *) echo "Please input valid ID!"
    ;;

  esac

else
  echo "No input file in this directory."

fi
