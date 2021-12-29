#!/usr/bin/env bash
set -eou pipefail

pyhelp=0
quiet=0
args=("$@")
for i in "${!args[@]}"
do
  if [[ ${args[$i]} == -h || ${args[$i]} == --help ]]; then
    pyhelp=1
    break
  fi

  if [[ ${args[$i]} == -q ]]
  then
    quiet=1
  fi

  if [[ ${args[$i]} == *.py ]]; then
    pre_file_args=${args[@]:0:$i}
    file=${args[$i]}
    post_file_args=${args[@]:$i + 1:${#args[@]}}
    break
  fi
done

if [[ $pyhelp -eq 1 ]]; then
cat << _EOT_
py [-h] [python arguments] [file.py] [file.py arguments]

py = mypy + isort + black + python

Without argument file:   Run py recursively in the current directory.
With argument file:      Run py on the provided file.

\`py\` acts the same as \`python\` otherwise.

-h, ---help   show this message
-q            supresses non-error output
_EOT_
exit 1
fi

if [[ $PY == "" ]]; then
  echo PY env variable not set, default-ing to python3
  PY="python3"
fi

if [[ $quiet -eq 1 ]]
  then
    # quiet flag is the same for python3, isort, and black
    # mypy doesn't have a quiet flag :( see workaround below
    quiet_flag="-q"
  else
    quiet_flag=""
fi

# TODO manual set -x
# TODO mypy color output --color-output
# just ignore all arguments except -q if no file.py given ¯\_(ツ)_/¯

run_mypy () {
  set +e
  local mypy_output=$($PY -m mypy $1)
  local mypy_exit_code=$?

  if [[ $mypy_exit_code -eq 0 && $quiet -eq 0 ]]
  then
    echo $mypy_output
  fi

  if [[ $mypy_exit_code -eq 1 ]]
  then
    echo $mypy_output
    exit 1
  fi
  set -e
}

if [[ $# -eq 0 ]] || \
[[ $# -eq 1 && $1 == -q ]] || \
[[ $# -eq 1 && $1 == -h || $# -eq 1 && $1 == --help ]]
  then
    #set -x
    run_mypy .
    $PY -m isort $quiet_flag .
    $PY -m black $quiet_flag .
  else
    #set -x
    run_mypy $file
    $PY -m isort $quiet_flag $file
    $PY -m black $quiet_flag $file
    # don't pass the quiet flag to python, I'm exploiting
    # the fact our quiet flag is the same as python's "-q"
    # so it's in pre_file_args already
    $PY $pre_file_args $file $post_file_args
fi
