#!/usr/bin/env bash
set -eou pipefail
shopt -s expand_aliases
alias set_TY_TYPE_CHECKER="eval $(py parse-toml.py)"
set_TY_TYPE_CHECKER
echo $TY_TYPE_CHECKER
