#!/bin/bash

path=$PWD/pi_csvs

cd $path

for file in $path/*; do
  only_app="${file##*/}"
  app=$(echo $only_app | cut -d '-' -f 1)
  $(python3 ../chart.py $app $PWD/$app*)
done
