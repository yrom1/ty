#!/usr/bin/env bash
set -oux pipefail
./ry

./ry -h
./ry --help

./ry test-good.py
./ry test-bad.py
./ry test-good.py 1 2 3
./ry test-bad.py 1 2 3
./ry -O test-good.py 1 2 3
./ry -O test-bad.py 1 2 3

./ry -q
./ry -q test-good.py 1 2 3
./ry -q test-bad.py 1 2 3
./ry -q -O test-good.py 1 2 3
./ry -q -O test-bad.py 1 2 3

cat test-tty-stdin.py | ./ry test-tty-stdin.py
./ry -
./ry -q -

./ry -c "print(1)"
./ry -c "print(1);   print(2)"
./ry -q -c "print(1);   print(2)"

rm -rf .venv-test/
./ry -m venv .venv-test
rm -rf .venv-test/
./ry -q -m venv .venv-test
rm -rf .venv-test/

./ry -X importtime -c 'import asyncio'
./ry -q -X importtime -c 'import asyncio'

./ry -V
./ry -V -V
./ry -V -V -V # does the same as -V -V

# these tests can fail if you don't actually have the 3.X verion installed which
# is correct, ry should fail by returning py's message which looks like this:
# $ py -3.8
# No executable found for Python 3.8
./ry -3 -V
./ry -3.8 -V
./ry -3.9 -V
./ry -3.10 -V
./ry -3.9 -O -i test-good.py 1 2 3
./ry -3.9 -q -O -i test-good.py 1 2 3
./ry -3.9 -O -i -q test-good.py 1 2 3
