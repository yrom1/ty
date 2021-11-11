# py
Mypy, Black, isort, Python, all in one `py` command. 

# Usage

You can use `py` bare to run `mypy`, `black`, and `isort` in your current directory to recursively format the files:

```bash
py
```

Or you can pass a Python file to run that file after doing the formatting above:

```bash
py hello.py
```

# Setup

For Ubuntu 20.04 LTS:

```bash
chmod +x setup
source ./setup
```

Then reboot. That's it.

If you switch to a different Python virtual environment, you'll need to reinstall `Black`, `mypy`, and `isort`. Either manually, or with:

```
pip3 install -r requirements.txt
```

