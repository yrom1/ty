#!/usr/bin/env bash
set -eoux pipefail
filename=${1:-.}
if [ $# -eq 0 ]
    then
        mypy .
        python3 -m black .
        python3 -m isort .
        exit 0
    else
        python3 -m mypy $filename
        python3 -m black $filename
        python3 -m isort $filename
        python3 $filename
        exit 0
fi
