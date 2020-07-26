#!/bin/sh
#xlsx2csv -p "" -I "Data" -a FILENAME.xlsx | sed -e "4,$ s/Data//g" -e "4,$ s/Time,Temperature//g" -e '/^$/d' > CSVNAME.csv
echo "Please input Sensor ID!"
read SID

INPUT_FILE=$SID*.xlsx
echo $INPUT_FILE

case "$SID" in
  T0*)
  xlsx2csv -p "" -I "Data" -a $INPUT_FILE | sed -e "4,$ s/Data//g" -e "4,$ s/Time,Temperature//g" -e '/^$/d' > "$SID-full-obs.csv"
  ;;
  TD0*)
  xlsx2csv -p "" -I "Data" -a $INPUT_FILE| sed -e "4,$ s/Data//g" -e "4,$ s/Time,Temperature,Pressure,Sea pressure,Depth//g" -e '/^$/d' > "$SID-full-obs.csv"
  ;;
  *) echo "Please input valid ID!"
  ;;
esac

