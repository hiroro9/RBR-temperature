#!/bin/sh
#xlsx2csv -p "" -I "Data" -a FILENAME.xlsx | sed -e "4,$ s/Data//g" -e "4,$ s/Time,Temperature//g" -e '/^$/d' > CSVNAME.csv
xlsx2csv -p "" -I "Data" -a T01*.xlsx | sed -e "4,$ s/Data//g" -e "4,$ s/Time,Temperature//g" -e '/^$/d' > T01.csv
