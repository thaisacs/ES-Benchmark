#!/bin/bash

arg_parse() {
  len=${#args[@]}
  efs_ip=${args[0]}
  dest=${args[1]}
  type_vm=${args[2]}
  num_vm=${args[3]}
  bench_name=${args[4]}
  app_name=${args[5]}
}

init_cluster() {
  cluster=cluster-${bench_name}-${type_vm}-${num_vm}x
  clapp cluster start $cluster --extra "efs_ip=${efs_ip}"
  cluster_id=$(clapp cluster list | grep id | cut -d' ' -f2)
}

args=("$@")


arg_parse
init_cluster

for ((i=5; i<len; i++)); do
  results_dir=experimental_results/${args[$i]}/${type_vm}-${num_vm}/${now}/$(date +"%m-%d-%y-%T")
  mkdir -p ${results_dir}
  clapp cluster action ${cluster_id} ${bench_name}-group run --extra "app_name=${args[$i]}" "num_np=${num_vm}"
  clapp cluster action ${cluster_id} ${bench_name}-group fetch-results --extra "dir=${dest}"
  results=node-*/home/ubuntu/*/experiments/results/*
  mv ${results} ${results_dir}
done

clapp cluster stop ${cluster_id}
rm -r node*

#clapp cluster start cluster-npb.comp-t3.large-2x --extra "my_ip=172.31.4.213"
#clapp cluster stop cluster-104
