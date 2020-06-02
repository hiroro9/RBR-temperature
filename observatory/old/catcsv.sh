#!/bin/sh

OUTPUT="TD01"

CSV=".csv"
echo -n Input Sheet:
read PAGE

S="Sheet"

for SEN in `seq 1 $PAGE`
  do
    cat $S${SEN}$CSV | sed -e '1d' >> $OUTPUT$CSV
  done

