#!/usr/bin/env bash
set -oux pipefail
./py

./py -h
./py --help

./py test.py
./py test.py 1 2 3
./py -O test.py 1 2 3

./py -q
./py -q test.py 1 2 3
./py -q -O test.py 1 2 3
