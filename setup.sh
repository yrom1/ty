#!/usr/bin/env bash
set -eou pipefail

sudo mkdir -p /usr/local/ty
sudo cp ty /usr/local/ty
sudo chmod +x /usr/local/ty/ty
sudo cp parse-toml.py /usr/local/ty
set +e
grep -q 'export PATH=\"/usr/local/ty:\$PATH\"' ~/.bash_profile
grep_return=$?
set -e
if [[ $grep_return == 1 ]]; then
    echo "export PATH=\"/usr/local/ty:\$PATH\"" >> ~/.bash_profile
fi
set +H
printf "🐍 success! restart terminal to use ty\n"
