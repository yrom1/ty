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
+ python3 -m mypy test.py
Success: no issues found in 1 source file
+ python3 -m isort test.py
+ python3 -m black test.py
All done! ✨ 🍰 ✨
1 file left unchanged.
+ python3 -i -O test.py 1 2 3
['test.py', '1', '2', '3']
False
>>>
```

`ty` acts like `py`, passing arguments as expected.

# Setup

`ty` depends on [py](https://github.com/brettcannon/python-launcher) to find the newest python version to use, install `py` first.

Then, for Ubuntu 20.04 LTS:

```bash
chmod +x setup
./setup
```

That's it!
