import subprocess


def shell_output(cmd: str) -> str:
    process = subprocess.run(cmd.split(), capture_output=True)
    return (process.stderr.decode("utf-8") + process.stdout.decode("utf-8")).strip()


def file_contents(filename: str) -> str:
    with open(filename, "r") as f:
        ans = f.read()
    return ans.strip()


EXAMPLE_GOOD_CMD = "./ty -O ./examples/good/test-good.py 1 2 3"
EXAMPLE_GOOD_OUTPUT = shell_output(EXAMPLE_GOOD_CMD)
EXAMPLE_BAD_CMD = "./ty ./examples/bad/test-bad.py"
EXAMPLE_BAD_OUTPUT = shell_output(EXAMPLE_BAD_CMD)
EXAMPLE_GOOD_QUIET_CMD = "./ty -O -q ./examples/good/test-good.py 1 2 3"
EXAMPLE_GOOD_QUIET_OUTPUT = shell_output(EXAMPLE_GOOD_QUIET_CMD)
EXAMPLE_TERMINAL_CMD = "./ty -"
EXAMPLE_TERMINAL_OUTPUT = """
Python 3.10.2 (main, Feb  2 2022, 05:51:25) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
""".strip()
FILE_TEST_GOOD = file_contents("./examples/good/test-good.py")
FILE_META_SETUP = file_contents("./meta_setup.sh")
FILE_PYPROJECT_TOML = file_contents("./pyproject.toml")

README = rf"""
# ty
`ty` = `mypy|pyright|pytype` + `isort` + `black` + `py`, in one command.

# Usage

You can use the command `ty` to run `mypy`, `isort`, and `black` in the current directory recursively; Or, you can pass a Python file to `ty` to run `mypy`, `isort`, and `black` in that directory recursively, and then execute the file with `python3` (via [py](https://github.com/brettcannon/python-launcher)).

# Example

Given this file, `test-good.py` in a folder by itself:

```py
{FILE_TEST_GOOD}
```

After setup, running `{EXAMPLE_GOOD_CMD}` will give:

```
$ {EXAMPLE_GOOD_CMD}
{EXAMPLE_GOOD_OUTPUT}
```

`ty` acts like `py`, passing arguments as expected—with one exception, a bare `ty` will recursively run `ty` in the current directory:

```
$ {EXAMPLE_BAD_CMD}
{EXAMPLE_BAD_OUTPUT}
```

To access the terminal you can use a `{EXAMPLE_TERMINAL_CMD}`:

```
$ {EXAMPLE_TERMINAL_CMD}
{EXAMPLE_TERMINAL_OUTPUT}
```

You can also suppress non-error messages from `mypy`, `black`, `isort`, and `py` with `-q`:

```
$ {EXAMPLE_GOOD_QUIET_CMD}
{EXAMPLE_GOOD_QUIET_OUTPUT}
```

One can enable using a different type checker with a `pyproject.toml` file:

```
{FILE_PYPROJECT_TOML}
```

Currently [mypy](http://mypy-lang.org/), [pyright](https://github.com/microsoft/pyright), [pytype](https://google.github.io/pytype/) are supported, `mypy` being the default.

# Setup

`ty` depends on [py](https://github.com/brettcannon/python-launcher) to find the newest python version to use, install `py` first.

Then, to install:

```bash
{FILE_META_SETUP}
```

That's it! (For macOS also run `brew install coreutils`).

Completely optionally... if you want `pyright` to load faster you can install it with `npm`, otherwise `ty` defaults to the slower `pip`'ed installed `pyright`.

# In-Frequently Asked Questions (IFAQ)

Q: What does `ty` stand for?

A: `ty` stands for ty~~pe~~ and t~~id~~y.
"""

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(README.strip())
