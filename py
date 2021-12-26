#!/usr/bin/env bash
# USAGE: ./py test.py hi
# TODO cant parse things between ./py and test.py like for example:
#      in "./py -i test.py hi" the -i flag is helpful sometimes
set -eou pipefail
args="${@:2}"
filename=$1
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
        python3 $filename $args
fi
