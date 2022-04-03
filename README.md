# ty
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

After setup, running `./ty -O ./examples/good/test-good.py 1 2 3` will give:

```
$ ./ty -O ./examples/good/test-good.py 1 2 3
+ py -m isort .
+ py -m black .
All done! ✨ 🍰 ✨
8 files left unchanged.
+ py -O ./examples/good/test-good.py 1 2 3
+ py -m mypy --pretty .
Skipped 1 files
['./examples/good/test-good.py', '1', '2', '3']
False
```

`ty` acts like `py`, passing arguments as expected—with one exception, a bare `ty` will recursively run `ty` in the current directory:

```
$ ./ty ./examples/bad/test-bad.py
+ py -m isort .
+ py -m black .
All done! ✨ 🍰 ✨
8 files left unchanged.
+ py ./examples/bad/test-bad.py
+ py -m mypy --pretty .
Skipped 1 files
['./examples/bad/test-bad.py']
True
```

To access the terminal you can use a `./ty -`:

```
$ ./ty -
Python 3.10.2 (main, Feb  2 2022, 05:51:25) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can also suppress non-error messages from `mypy`, `black`, `isort`, and `py` with `-q`:

```
$ ./ty -O -q ./examples/good/test-good.py 1 2 3
['./examples/good/test-good.py', '1', '2', '3']
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
chmod +x setup
./setup
py -m pip install -r requirements.txt
```

That's it! (For macOS also run `brew install coreutils`).

Completely optionally... if you want `pyright` to load faster you can install it with `npm`, otherwise `ty` defaults to the slower `pip`'ed installed `pyright`.

# In-Frequently Asked Questions (IFAQ)

Q: What does `ty` stand for?

A: `ty` stands for ty~~pe~~ and t~~id~~y.