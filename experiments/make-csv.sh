#!/bin/bash

for app in experimental_results/*; do
  for cfg in $app/*; do
    for file in $cfg/*; do
      for date in $file/*; do
        echo $date
      done
    done
  done
done
