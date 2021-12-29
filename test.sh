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

./py -c "print(1)"
./py -c "print(1);   print(2)"
./py -q -c "print(1);   print(2)"

rm -rf .venv-test/
./py -m venv .venv-test
rm -rf .venv-test/
./py -m -q venv .venv-test
rm -rf .venv-test/
./py -q -m venv .venv-test
rm -rf .venv-test/

# TODO
# ./py -X importtime -c 'import asyncio'
