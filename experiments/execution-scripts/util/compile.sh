#!/bin/bash

arg_parse() {
  len=${#args[@]}
  efs_ip=${args[0]}
  type_vm=${args[1]}
  bench_name=${args[2]}
}

init_cluster() {
  cluster=cluster-${bench_name}.comp-${type_vm}
  clapp cluster start $cluster --extra "efs_ip=${efs_ip}"
  cluster_id=$(clapp cluster list | grep id | cut -d' ' -f2)
}

end_cluster() {
  clapp cluster stop ${cluster_id}
}

args=("$@")

arg_parse
init_cluster
end_cluster
