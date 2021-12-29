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
