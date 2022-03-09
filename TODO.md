Add support to declare the engine in a .toml file like this:
```
[tool.ty]
type_checker = pyright
```
I find I want to switch between mypy and pyright sometimes,
it would be nice to have it as a project setting.

It would also be good to just have it as a command line flag:
```
ty --mypy leetcode.py
ty --pyright leetcode.py
```
But then we break the concept of just acting like `py`...
And you have to deal with conflicts, does project or command line
take priority, maybe issue a warning and go with cmd line flag.

---
