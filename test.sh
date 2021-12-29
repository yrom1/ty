#!/usr/bin/env bash
set -oux pipefail
./py

./py -h
./py --help

./py test-good.py
./py test-bad.py
./py test-good.py 1 2 3
./py test-bad.py 1 2 3
./py -O test-good.py 1 2 3
./py -O test-bad.py 1 2 3

./py -q
./py -q test-good.py 1 2 3
./py -q test-bad.py 1 2 3
./py -q -O test-good.py 1 2 3
./py -q -O test-bad.py 1 2 3

cat test-tty-stdin.py | ./py test-tty-stdin.py
./py -
./py -q -
