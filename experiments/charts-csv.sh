#!/bin/bash

mkdir pi_csvs
path=$PWD/pi_csvs

cd experimental_results

for app in *; do
  for cfg in $app/*; do
    for date in $cfg/*; do
      only_cfg="${cfg##*/}"
      for file in $date/*; do
        if [ "${file##*.}" = "out" ]; then
          $(cat ${file} | grep -P "^(?=.*MO833)(?=.*Iteration)" | cut -d " " -f 2 >> $path/$app-$only_cfg.csv )
          #$(cat ${file} | grep -P "^(?=.*MO833)(?=.*Paramount)(?=.*Iteration)" | cut -d " " -f 3  >> $path/$app-$only_cfg.csv )
        fi
      done
    done
  done
done
