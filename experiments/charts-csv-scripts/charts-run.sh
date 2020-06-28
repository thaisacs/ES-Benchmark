#!/bin/bash

mkdir -p charts
cd ../experimental_results
path=$PWD

for app in *; do
  apps=""
  for cfg in $app/*; do
    only_cfg="${cfg##*/}"
    for date in $cfg/*; do
      for file in $date/*; do
        if [ "${file##*.}" = "csv" ]; then
          apps="$apps $file"
        fi
      done
    done
  done
  python3 ../charts-csv-scripts/util/chart-relative.py $app $apps
  python3 ../charts-csv-scripts/util/chart.py $app $apps
done
