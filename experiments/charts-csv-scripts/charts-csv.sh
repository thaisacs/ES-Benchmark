#!/bin/bash

cd ../experimental_results

for app in *; do
  for cfg in $app/*; do
    for date in $cfg/*; do
      only_cfg="${cfg##*/}"
      for file in $date/*; do
        if [ "${file##*.}" = "out" ]; then
          $(cat ${file} | grep -P "^(?=.*MO833)(?=.*Iteration)" | cut -d " " -f 3 > ${file}.csv )
        fi
      done
    done
  done
done
