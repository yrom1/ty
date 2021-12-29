#!/usr/bin/env bash
set -eou pipefail

start_console=0
m_arg=0
c_arg=0
quiet=0
file_flag=0
args=("$@")
for i in "${!args[@]}"
do
  if [[ ${args[$i]} == -h || ${args[$i]} == --help ]]; then
    cat << _EOT_
Usage: py [option] ... [file | -] [arg] ...
py = mypy + isort + black + python, in one command

Without file argument:   Run py recursively in the current directory
With one file argument:  Run py on the provided file, py acts the same
                         as the python3 command for files

Options and arguments:
-h     : print this message and exit (also ---help)
-q     : supresses non-error non-result output from mypy, isort, black, python
         and py itself
[...]  : other options passed to py are passed to python when a file is present
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg    : arguments passed to program in sys.argv[1:]

Environment variable:
PY     : Location of Python3 command, if not set defaults to \`python3\`
_EOT_
    exit 0
  fi

  if [[ ${args[$i]} == - ]]; then
    start_console=1
  fi

  if [[ ${args[$i]} == -m ]]; then
    m_arg=1
  fi

  if [[ ${args[$i]} == -c ]]; then
    c_arg=1
  fi

  if [[ ${args[$i]} == -q ]]; then
    quiet=1
  fi

  if [[ ${args[$i]} == *.py ]]; then
    file_flag=1
    pre_file_args=${args[@]:0:$i}
    file=${args[$i]}
    post_file_args=${args[@]:$i + 1:${#args[@]}}
    break
  fi
done

arg_sum=$(( $start_console + $m_arg + $c_arg + $file_flag))
if [[ $arg_sum -gt 1 ]]; then
  echo -c, -m, *.py, - args mutually exclusive
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

if [[ $start_console -eq 1 ]]; then
  tty_cmd="$PY $quiet_flag -"
  if [[ $quiet -eq 0 ]]; then
    echo + $tty_cmd
  fi
  $tty_cmd
  exit
fi


if [[ $c_arg -eq 1 || $m_arg -eq 1 ]]; then
  if [[ $quiet -eq 0 ]]; then
    echo + $PY "$@"
  fi
  $PY "$@"
  exit
fi

# TODO implement all python3's functionality:
# [-c cmd | -m mod | file | -]
# just ignore all arguments except -q if no file.py given ¯\_(ツ)_/¯

run_mypy () {
  if [[ $quiet -eq 0 ]]; then
      printf "+ $PY -m mypy $1\n"
  fi

  set +e
  # not using local so exit code reflects mypy
  mypy_output=$($PY -m mypy --pretty $1)
  mypy_exit_code=$?
  set -e

  if [[ $mypy_exit_code -eq 0 && $quiet -eq 0 ]]
  then
    printf "$mypy_output\n"
  fi

  if [[ $mypy_exit_code -eq 1 ]]
  then
    printf "$mypy_output\n"
    exit 1
  fi
}

set_x_if_allowed() {
  if [[ $quiet -eq 0 ]]; then
      set -x
  fi
}

if [[ $# -eq 0 ]] || \
[[ $# -eq 1 && $1 == -q ]]
  then
    run_mypy .
    set_x_if_allowed
    $PY -m isort $quiet_flag .
    $PY -m black $quiet_flag .
  else
    run_mypy $file
    set_x_if_allowed
    $PY -m isort $quiet_flag $file
    $PY -m black $quiet_flag $file
    # don't pass the quiet flag to python, I'm exploiting
    # the fact our quiet flag is the same as python's "-q"
    # so it's in pre_file_args already
    $PY $pre_file_args $file $post_file_args
fi
