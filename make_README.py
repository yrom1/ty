import subprocess


def shell_output(cmd: str) -> str:
    ans = subprocess.run(cmd.split(), capture_output=True)
    return ans.stdout + ans.stderr


EXAMPLE_GOOD_CMD = "./ty -i -O ./examples/good/test-good.py 1 2 3"
EXAMPLE_GOOD_OUTPUT = shell_output(EXAMPLE_GOOD_CMD)
EXAMPLE_BAD_CMD = "./ty ./examples/bad/test-bad.py"
EXAMPLE_BAD_OUTPUT = shell_output(EXAMPLE_BAD_CMD)
EXAMPLE_GOOD_QUIET_CMD = "./ty -i -O -q ./examples/good/test-good.py 1 2 3"
EXAMPLE_GOOD_QUIET_OUTPUT = shell_output(EXAMPLE_GOOD_QUIET_CMD)
EXAMPLE_TERMINAL_CMD = "./ty -"
EXAMPLE_TERMINAL_OUTPUT = shell_output(EXAMPLE_TERMINAL_CMD)


with open("meta_setup.sh", "r") as f:
    META_SETUP = f.read()

README = rf"""
# ty
`ty` = `mypy|pyright|pytype` + `isort` + `black` + `py`, in one command.

# Usage

You can use the command `ty` to run `mypy`, `isort`, and `black` in the current directory recursively; Or, you can pass a Python file to `ty` to run `mypy`, `isort`, and `black` in that directory recursively, and then execute the file with `python3` (via [py](https://github.com/brettcannon/python-launcher)).

# Example

Given this file, `test.py` in a folder by itself:

```py
import sys

print(sys.argv)
print(__debug__) # default is True
```

After setup, running `ty -i -O test.py 1 2 3` will give:

```
$ {EXAMPLE_GOOD_CMD}
{EXAMPLE_GOOD_OUTPUT}
```

`ty` acts like `py`, passing arguments as expected—with one exception, a bare `ty` will recursively run `ty` in the current directory:

```
$ {EXAMPLE_BAD_CMD}
{EXAMPLE_BAD_OUTPUT}
```

To access the terminal you can use a `-`:

```
$ ty -
Python 3.8.10 (default, Nov 26 2021, 20:14:08)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can also suppress non-error messages from `mypy`, `black`, `isort`, and `py` with `-q`:

```
$ {EXAMPLE_GOOD_QUIET_CMD}
{EXAMPLE_GOOD_QUIET_OUTPUT}
```

One can enable using a different type checker with a `pyproject.toml` file:

```
[tool.ty]
type_checker = "pyright"
```

Currently [mypy](http://mypy-lang.org/), [pyright](https://github.com/microsoft/pyright), [pytype](https://google.github.io/pytype/) are supported, `mypy` being the default.

# Setup

`ty` depends on [py](https://github.com/brettcannon/python-launcher) to find the newest python version to use, install `py` first.

Then, to install:

```bash
{META_SETUP}
```

That's it! (For macOS also run `brew install coreutils`).

Completely optionally... if you want `pyright` to load faster you can install it with `npm`, otherwise `ty` defaults to the slower `pip`'ed installed `pyright`.

# Infrequently Asked Questions (IFAQ)

Q: What does `ty` stand for?

A: `ty` stands for ty~~pe~~ and t~~id~~y.
"""

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(README.strip())
