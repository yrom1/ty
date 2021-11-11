#!/usr/bin/env bash
set -eou pipefail
if [ $# -eq 0 ]
    then
        echo "Must pass filename as argument."
        exit 0
fi

filename=$1
set -x
mypy $filename
black $filename
isort $filename
python3 $filename
