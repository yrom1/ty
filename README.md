# ty
`ty` = `mypy` + `isort` + `black` + `py`, in one command.

# Usage

You can use the command `ty` to run `mypy`, `isort`, and `black` in the current directoty recursively; Or, you can pass a Python file to `ty` to run `mypy`, `isort`, and `black` on that file, and then execute the file with `python3` (via [py](https://github.com/brettcannon/python-launcher)).

# Example

Given this file, `test.py`:

```py
import sys

print(sys.argv)
print(__debug__) # default is True
```

After setup, running `ty -i -O test.py 1 2 3` will give:

```
$ ty -i -O test.py 1 2 3
+ py -m mypy test.py
Success: no issues found in 1 source file
+ py -m isort test.py
+ py -m black test.py
All done! ✨ 🍰 ✨
1 file left unchanged.
+ py -i -O test.py 1 2 3
['test.py', '1', '2', '3']
False
>>>
```

`ty` acts like `py`, passing arguments as expected—with one exception, a bare `ty` will recursively run `ty` in the current directory:

```
$ ty
+ py -m mypy .
test-bad.py:3: error: Incompatible types in assignment (expression has type
"str", variable has type "int")
    a: int = "a"
             ^
Found 1 error in 1 file (checked 3 source files)
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
$ ty -q -i -O test-good.py 1 2 3
['test-good.py', '1', '2', '3']
False
>>>
```

# Setup

`ty` depends on [py](https://github.com/brettcannon/python-launcher) to find the newest python version to use, install `py` first.

Then, to install:

```bash
chmod +x setup
./setup
```

That's it!
