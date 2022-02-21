# ry
`ry` = `pyright` + `isort` + `black` + `py`, in one command

# Usage

You can use the command `ry` to run `pyright`, `isort`, and `black` in the current directory recursively; Or, you can pass a Python file to `ry` to run `pyright`, `isort`, and `black` on that file, and then execute the file with Python.

# Setup

`ry` depends on [py](https://github.com/brettcannon/python-launcher) to find the newest python version to use, install [py](https://github.com/brettcannon/python-launcher) first.

Then, for Ubuntu 20.04 LTS:

```bash
chmod +x setup
./setup
```

That's it!
