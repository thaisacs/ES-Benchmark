#!/bin/bash

my_csv=$PWD/experimental_results.summary.csv

echo "test-case,cfg,date,total_time-time,total_time-main,beta,avg-PIs,n-PIs,1st-PI,2nd-PI,avg(2-6),avg(2-11)" > $my_csv

cd experimental_results

for app in *; do
  for cfg in $app/*; do
    for date in $cfg/*; do
      only_cfg="${cfg##*/}"
      only_date="${date##*/}"
      for file in $date/*; do
        if [ "${file##*.}" = "time" ]; then
          wall_time=$(head -n 1 ${file} | cut -d " " -f 2)
        elif [ "${file##*.}" = "out" ]; then
          main_time=$(cat ${file} | grep -P '^(?=.*MO833)(?=.*Total)' | cut -d " " -f 3 | cut -d "," -f 2)
          betas=$(cat ${file} | grep -P '^(?=.*MO833)(?=.*Beta)' | cut -d " " -f 2)
          for i in 1 2 3 4 5 6 7 8; do
            line=$(echo $betas | cut -d " " -f ${i})
            if [[ ${line} == *,0,* ]]; then
              beta=$(echo $line | cut -d "," -f 3)
              break
            fi
          done
          avgs=$(cat ${file} | grep -P '^(?=.*MO833)(?=.*PI avg)' | cut -d " " -f 3)
          for i in 1 2 3 4 5 6 7 8; do
            line=$(echo $avgs | cut -d " " -f ${i})
            if [[ ${line} == *,0,* ]]; then
              avg=$(echo $line | cut -d "," -f 3)
              n=$(echo $line | cut -d "," -f 4)
              break
            fi
          done
        fi
      done
      echo $app,$only_cfg,$only_date,$wall_time,$main_time,$beta,$avg,$n,0,0,0,0 >> $my_csv
    done
  done
done
