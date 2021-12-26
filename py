#!/usr/bin/env bash
# USAGE: ./py -i test.py
set -eou pipefail
length=$(($#-1))
args=${@:1:$length}
filename="${@: -1}"
# echo args $args
# echo filename $filename
if [ $# -eq 0 ]
    then
        set -x
        python3 -m mypy .
        python3 -m isort .
        python3 -m black .
    else
        set -x
        python3 -m mypy $filename
        python3 -m isort $filename
        python3 -m black $filename
        python3 $args $filename
fi
