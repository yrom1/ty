run_tests() {
    ./ty test-good.py
    ./ty test-bad.py
}

py make-toml.py "mypy"
run_tests
py make-toml.py "pyright"
run_tests
py make-toml.py "pytype"
run_tests
