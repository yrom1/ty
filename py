#!/usr/bin/env bash
# USAGE: ./py -i test.py hi
set -eou pipefail

args=("$@")
for i in "${!args[@]}"
do
  if [[ ${args[$i]} == *.py ]]; then
    echo found python file at $i
    pre_file_args=${args[@]:0:$i}
    file=${args[$i]}
    post_file_args=${args[@]:$i + 1:${#args[@]}}
  fi
done

if [ $# -eq 0 ]
  then
    set -x
    python3 -m mypy .
    python3 -m isort .
    python3 -m black .
  else
    set -x
    python3 -m mypy $file
    python3 -m isort $file
    python3 -m black $file
    python3 $pre_file_args $file $post_file_args
fi
