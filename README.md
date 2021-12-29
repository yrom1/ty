# py
`py` = `mypy` + `isort` + `black` + `python3`, in one command.

# Usage

You can use the command `py` to run `mypy`, `isort`, and `black` in the current directory recursively; Or, you can pass a Python file to `py` to run `mypy`, `isort`, and `black` on that file, and then execute the file with `python3`.

# Example

Given this file, `test.py`:

```py
import sys

print(sys.argv)
print(__debug__) # default is True
```

After setup, running `py -i -O test.py 1 2 3` will give:

```
$ py -i -O test.py 1 2 3
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

`py` acts like `python3`, passing arguments as expected.

# Setup

For Ubuntu 20.04 LTS:

```bash
chmod +x setup
./setup
```

That's it!
