#!/usr/bin/env bash
set -eou pipefail

# - mypy -
py -m pip install mypy

# - pytype -
py -m pip install pytype

# - pyright -
# TODO this can only be ran by root
# https://www.ubuntuupdates.org/ppa/nodejs_12.x
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
sudo sh -c "echo deb https://deb.nodesource.com/node_12.x impish main > /etc/apt/sources.list.d/nodesource.list"
sudo apt-get update
# TODO when was the fix-missing needed?
sudo apt-get update --fix-missing
sudo apt-get install nodejs
sudo apt-get update --fix-missing
sudo apt install npm
sudo apt-get update --fix-missing
sudo npm install -g pyright

# - test -
# npx pyright --help
# py -m pytype --help
# py -m mypy --help
