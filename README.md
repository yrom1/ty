# py
Mypy, Black, isort, Python, all in one `py` command. 

# Usage

You can use `py` bare to recursively run `mypy`, `black`, and `isort` in the current directory:

```
$ py
+ mypy .
Success: no issues found in 1 source file
+ python3 -m isort .
Fixing /home/ryan/py/hello.py
Skipped 2 files
+ python3 -m black .
reformatted hello.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

Or, you can pass a Python file to `py` to run that file, after doing the formatting and type checking described above:

```
$ py hello.py 
+ python3 -m mypy hello.py
Success: no issues found in 1 source file
+ python3 -m isort hello.py
Fixing /home/ryan/py/hello.py
+ python3 -m black hello.py
reformatted hello.py
All done! ✨ 🍰 ✨
1 file reformatted.
+ python3 hello.py
Hello, bash!
```

Note that even when you pass a Python file, `py` still formats and type checks all files recusively in the current directory.

# Setup

For Ubuntu 20.04 LTS:

```bash
chmod +x setup
source ./setup
```

That's it.

If you switch to a different Python virtual environment, you'll need to reinstall `Black`, `mypy`, and `isort`. Either manually, or with:

```
pip3 install -r requirements.txt
```

