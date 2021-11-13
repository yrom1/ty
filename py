#!/usr/bin/env bash
set -eou pipefail
filename=${1:-_}
if [ $# -eq 0 ]
    then
        set -x
        mypy .
        python3 -m isort .
        python3 -m black .
    else
        set -x
        python3 -m mypy $filename
        python3 -m isort $filename
        python3 -m black $filename
        python3 $filename
fi
