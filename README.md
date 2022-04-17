# ty 🦆🧹
`ty` = `mypy|pyright|pytype` + `isort` + `black` + `py`, in one command.

# Usage

You can use the command `ty` to run `mypy`, `isort`, and `black` in the current directory recursively; Or, you can pass a Python file to `ty` to run `mypy`, `isort`, and `black` in that directory recursively, and then execute the file with `python3` (via [py](https://github.com/brettcannon/python-launcher)).

# Example

Given this file, `test-good.py` in a folder by itself:

```py
import sys

a: str = "a"
print(sys.argv)
print(__debug__)
```

After setup, running `ty -O test-good.py 1 2 3` will give:

```
$ ty -O test-good.py 1 2 3
🦆🧹 type checking
Success: no issues found in 1 source file
🦆🧹 sorting imports
Skipped 1 files
🦆🧹 formatting files
All done! ✨ 🍰 ✨
1 file left unchanged.
🦆🧹 executing python
['test-good.py', '1', '2', '3']
False
```

`ty` acts like `py`, passing arguments as expected—with one exception, a bare `ty` will recursively run `ty` in the current directory:

```
$ ty
🦆🧹 type checking
test-bad.py:3: error: Incompatible types in assignment (expression has type
"str", variable has type "int")
    a: int = "a"
             ^
Found 1 error in 1 file (checked 1 source file)
```

To access the terminal you can use a `ty -`:

```
$ ty -
Python 3.10.2 (main, Feb  2 2022, 05:51:25) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can also suppress non-error messages from `mypy`, `black`, `isort`, and `py` with `-q`:

```
$ ty -O -q test-good.py 1 2 3
['test-good.py', '1', '2', '3']
False
```

One can enable using a different type checker with a `pyproject.toml` file:

```
[tool.ty]
type_checker = "mypy"
```

Currently [mypy](http://mypy-lang.org/), [pyright](https://github.com/microsoft/pyright), [pytype](https://google.github.io/pytype/) are supported, `mypy` being the default.

# Setup

`ty` depends on [py](https://github.com/brettcannon/python-launcher) to find the newest python version to use, install `py` first.

Then, to install:

```bash
chmod +x setup.sh
./setup.sh
py -m pip install -r requirements.txt
```

That's it! (For macOS also run `brew install coreutils`).

Completely optionally... if you want `pyright` to load faster you can install it with `npm`, otherwise `ty` defaults to the slower `pip`'ed installed `pyright`.

# In-Frequently Asked Questions (IFAQ)

Q: What does `ty` stand for?

A: `ty` stands for ty~~pe~~ and t~~id~~y.