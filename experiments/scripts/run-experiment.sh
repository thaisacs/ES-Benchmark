#!/bin/bash

arg_parse() {
  len=${#args[@]}
  type_vm=${args[0]}
  num_vm=${args[1]}
  bench_name=${args[2]}
  app_name=${args[3]}
}

init_cluster() {
  cluster=cluster-${bench_name}-${type_vm}-${num_vm}x
  clapp cluster start $cluster
  cluster_id=$(clapp cluster list | grep id | cut -d' ' -f2)
}

args=("$@")

arg_parse
#init_cluster

for ((i=3; i<len; i++)); do
  results_dir=experimental_results/${args[$i]}/${type_vm}-${num_vm}/${now}/$(date +"%m-%d-%y-%T")
  mkdir -p ${results_dir}
  #clapp cluster action ${cluster_id} ${bench_name}-group run --extra "app_name=${args[$i]}" "num_np=${num_vm}"
  #clapp cluster action ${cluster_id} ${bench_name}-group fetch-results
  #results=node-*/home/ubuntu/*/experiments/results/*
  #mv ${results} ${results_dir}
  #rm -r ${results}
done

#clapp cluster stop ${cluster_id}
