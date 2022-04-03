If `ty` is used to run a file in a different folder, it uses the default `mypy`
because it can't find a `pyproject.toml` in the `$(realpath dirname $PWD)`.

Should it do this? Is it possible to find what module a script belongs to?
What happens for namespace packages?

---

Update `README.md` examples with the new API of always in the current directory.
Can I use a template engine to make it automatically, does Mako play well with
shell? Maybe just capture subprocess output?

---
